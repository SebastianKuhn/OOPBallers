import pymysql


def connect_to_sql():
    """
    This function return the parameters to connect to your MySQL.
    CHANGE INFO HERE
    :return:
    """
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='sqlproject',
                                 db='oopproject',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def insert_weather(conn, forecast):
    """
    Inserts the weather, found in "forecast" into your MySQL DB.
    :param conn:
    :param forecast:
    :return:
    """
    ins = """INSERT INTO weather (curr_summary, curr_temp, curr_humidity, curr_uvindex,
    day0_summary, day0_temp_high, day0_temp_low, day0_humidity, day0_uvindex,
    day1_summary, day1_temp_high, day1_temp_low, day1_humidity, day1_uvindex,
    day2_summary, day2_temp_high, day2_temp_low, day2_humidity, day2_uvindex, week_summary, requests_request_id)
    SELECT '{!s}', {!s}, {!s}, {!s}, '{!s}', {!s}, {!s}, {!s}, {!s}, '{!s}', {!s}, {!s}, {!s}, {!s}, '{!s}', {!s}, {!s},
    {!s}, {!s}, '{!s}', request_id FROM requests ORDER BY request_id DESC LIMIT 1
    
    """.format(forecast[0][0],
                                                              forecast[0][1],
                                                              forecast[0][2],
                                                              forecast[0][3],
                                                              forecast[0][4],
                                                              forecast[0][5],
                                                              forecast[0][6],
                                                              forecast[0][7],
                                                              forecast[0][8],
                                                              forecast[0][9],
                                                              forecast[0][10],
                                                              forecast[0][11],
                                                              forecast[0][12],
                                                              forecast[0][13],
                                                              forecast[0][14],
                                                              forecast[0][15],
                                                              forecast[0][16],
                                                              forecast[0][17],
                                                              forecast[0][18],
                                                              forecast[0][19])
    try:
        with conn.cursor() as cursor:
            cursor.execute(ins)
        conn.commit()
    except:
        conn.rollback()

def select_weather(conn, req):
    """
    Selects weather data from your mysql according to a 'request_id"
    :param conn:
    :param req:
    :return:
    """
    sel = """SELECT * FROM weather WHERE requests_request_id = {}""".format(req)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            weather = cursor.fetchone()
    except:

        conn.rollback()
    return weather

def insert_request(conn, user_latitude, user_longitude, category):
    """
    Inserts the users latitude, longitude and chosen category into the respective mysql table.
    :param conn:
    :param user_latitude:
    :param user_longitude:
    :param category:
    :return:
    """
    ins = """INSERT INTO requests (updatetime, latitude, longitude, categories_category_id) 
            SELECT TIME(CURRENT_TIME()), {!s}, {!s}, category_id FROM categories WHERE category_id = {!s}""".format(user_latitude,
                                                                                                         user_longitude, category)

    try:
        with conn.cursor() as cursor:
            cursor.execute(ins)
        conn.commit()
    except:
        conn.rollback()


#    finally:
#        conn.close()

def insert_venues(conn, list_venues):
    """
    Inserts the venues, found through the YELP Api, into the respective table including the last request_id
    :param conn:
    :param list_venues:
    :return:
    """
    ins = """INSERT INTO venue (yelp_id, address, city, latitude, longitude, name, rating, url, phone, distance, requests_request_id)
    SELECT %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, request_id FROM requests ORDER BY request_id DESC LIMIT 1"""

    try:
        with conn.cursor() as cursor:
            cursor.executemany(ins, list_venues)
        conn.commit()
    except:
        conn.rollback()


#    finally:
#        conn.close()

def select_categories(conn):
    """
    Selects all categories saved in the category table
    :param conn:
    :return:
    """
    sel = """SELECT * FROM categories"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            cat = cursor.fetchall()
    except:
        conn.rollback()
    #    finally:
    #        conn.close()
    return cat


def select_requests(conn):
    """
    Selects all old requests from the request table
    :param conn:
    :return:
    """
    sel = """SELECT * FROM requests"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            req = cursor.fetchall()
    except:
        conn.rollback()
    #    finally:
    #        conn.close()
    return req


def select_request(conn):
    """
    Selects the last request entered
    :param conn:
    :return:
    """
    sel = """SELECT * FROM requests ORDER BY request_id DESC LIMIT 1"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            req = cursor.fetchone()
    except:
        conn.rollback()
    return req


def select_old_request(conn, request_id, filter, ascdesc, rownumber):
    """
    Selects all venues that belong to the given request according to a 'filter' = distance or rating, 'ascdesc' =
    whether it should be portrayed in ascending or descending order, 'rownumber' = how many rows will be displayed
    :param conn:
    :param request_id:
    :param filter:
    :param ascdesc:
    :param rownumber:
    :return:
    """
    sel ="""SELECT requests_request_id,  venue.venue_id, venue.address, venue.city, venue.latitude, venue.longitude, venue.name, venue.rating, venue.url, venue.phone, venue.distance, categories.category_name 
               FROM requests
               INNER JOIN categories ON  requests.categories_category_id=categories.category_id
               INNER JOIN venue ON requests.request_id= venue.requests_request_id
               WHERE venue.requests_request_id = {} order by {} {} limit {}""".format(request_id,
                                                                                      filter,
                                                                                      ascdesc,
                                                                                      rownumber)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            req = cursor.fetchall()
    except:
        conn.rollback()
    return req

def select_one(conn, venue_id):
    """
    This selects all info including category and request_id of a venue from the venue table according to a venue id
    :param conn:
    :param venue_id:
    :return:
    """
    sel = """SELECT requests_request_id,  venue.venue_id, venue.address, venue.city, venue.latitude, venue.longitude, venue.name, venue.rating, venue.url, venue.phone, venue.distance, categories.category_name 
              FROM requests
               INNER JOIN categories ON  requests.categories_category_id=categories.category_id
               INNER JOIN venue ON requests.request_id= venue.requests_request_id
               WHERE venue.venue_id = {}""".format(venue_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            ven = cursor.fetchone()
    except:
        conn.rollback()
    return ven

def select_req_acc_id(conn, req_id):
    """
    This selects everything from a request according to its id
    :param conn:
    :param req_id:
    :return:
    """
    sel = """SELECT * FROM requests WHERE request_id = {}""".format(req_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sel)
            req = cursor.fetchone()
    except:
        conn.rollback()
    return req

def delete_requests(conn):
    """
    This deletes all requests and the corresponding information for the requests that are older than 43200 seconds (12h)
    :param conn:
    :return:
    """
    delstate = """DELETE FROM requests WHERE TIMEDIFF(NOW(), requests.updatetime) > 43200"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(delstate)
        conn.commit()
    except:
        conn.rollback()
