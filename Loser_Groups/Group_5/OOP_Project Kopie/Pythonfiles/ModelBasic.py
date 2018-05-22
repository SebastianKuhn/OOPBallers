import Project.dao as dao


class Model():

    def __init__(self):
        self._connection = dao.connect_to_sql()

    @property
    def connection(self):
        return self._connection

    def insert_weather(self, forecast):
        dao.insert_weather(self.connection, forecast)

    def select_weather(self, req):
        weather = dao.select_weather(self.connection, req)
        return weather

    def insert_request(self, user_latitude, user_longitude, category):
        dao.insert_request(self.connection, user_latitude, user_longitude, category)

    def insert_venues(self, list_venues):
        dao.insert_venues(self.connection, list_venues)

    def select_categories(self):
        categories = dao.select_categories(self.connection)
        return categories

    def select_requests(self):
        requests = dao.select_requests(self.connection)
        return requests

    def select_request(self):
        request = dao.select_request(self.connection)
        return request

    def select_old_request(self, request_id, filter, ascdesc, row):
        requests = dao.select_old_request(self.connection, request_id, filter, ascdesc, row)
        return requests

    def select_one(self, venue_id):
        venue = dao.select_one(self.connection, venue_id)
        return venue

    def select_req_acc_id(self, req_id):
        req = dao.select_req_acc_id(self.connection, req_id)
        return req

    def delete_requests(self):
        dao.delete_requests(self.connection)

