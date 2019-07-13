from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'eason'
app.config['MYSQL_DATABASE_PASSWORD'] = 'migomigo'
app.config['MYSQL_DATABASE_DB'] = 'event'
app.config['MYSQL_DATABASE_HOST'] = 'migo-event-test.cbgmmh0zmnoq.us-east-2.rds.amazonaws.com'

mysql.init_app(app)


def insert_event(args):
    _user_id = args['user_id']
    _title = args['title']
    _description = args['description']
    _start_time = args['start_time']
    _end_time = args['end_time']
    _category_id = args['category_id']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_insert_event', (_user_id, _title, _description, _start_time, _end_time, _category_id))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        result = True
    else:
        result = False

    return result


def update_event(args):
    _id = args['id']
    _user_id = args['user_id']
    _title = args['title']
    _description = args['description']
    _start_time = args['start_time']
    _end_time = args['end_time']
    _category_id = args['category_id']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_update_event', (_id, _user_id, _title, _description, _start_time, _end_time, _category_id))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        result = True
    else:
        result = False

    return result


def get_events(user_id, sort_key, order, end_time_range):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_GetEventsByUserId', (user_id, sort_key, order, end_time_range))
    data = cursor.fetchall()
    items_list = []
    for item in data:
        i = {
            'Id': item[0],
            'UserId': item[1],
            'Title': item[2],
            'Description': item[3],
            'StartTime': item[4],
            'EndTime': item[5],
            'CategoryId': item[6]
        }
        items_list.append(i)
    # print(items_list)
    return items_list


def delete_events_by_user_id(user_id):
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "DELETE FROM event WHERE user_id = " + str(user_id)

    cursor.execute(sql)
    conn.commit()

