import pymysql
import requests


def getYelp():
    header = {
        "Authorization": 'Bearer qgwM2L8hevGosZuML4fFq-YD7wXtNUq4Qk2FHeo4N9mMpChXuXrk-ZxbUf1kqn1RThsMuPDk3g3oSFoiJfzSudnaNNqm4l9xMhAdmEiuWaWXE6rA9JkeOKFA_2bwWnYx'}
    r = requests.get('https://api.yelp.com/v3/categories', headers=header).json()
    return (r)

t = []
d = getYelp()

for i in d['categories']:
    if i['parent_aliases'] == []:
        t.append((
            i['title'],
            i['alias']
        ))
    else:
        pass

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='sqlproject',
                             db='oopproject',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

ins = """INSERT INTO categories (category_name, category_plain) VALUES (%s, %s)"""

with conn.cursor() as cursor:
    try:
        cursor.executemany(ins, t)
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()