from flask import Flask
from flask_restful import Api
from flask import request
import datetime
from datetime import timedelta
from db import event_db

app = Flask(__name__)
api = Api(app)

@app.route('/user/<user_id>/get_event_list', methods=['POST'])
def get_all_event(user_id):
    try:
        if "SortKey" in request.form:
            sort_key = request.form['SortKey']
        else:
            sort_key = 'Id'

        if "Order" in request.form:
            order = request.form['Order']
        else:
            order = 'desc'

        if "EndTimeRange" in request.form:
            end_time_range = request.form['EndTimeRange']
        else:
            end_time_range = datetime.datetime.now() - timedelta(hours=24)

        items_list = event_db.get_events(user_id, sort_key, order, end_time_range)
        return {'StatusCode': '200', 'Items': items_list}

    except Exception as e:
        return {'error': str(e)}

@app.route('/user/<user_id>/event', methods=['POST'])
def create_event_by_user_id(user_id):

    if "StartTime" in request.form:
        start_time = request.form['StartTime']
    else:
        start_time = datetime.datetime.now().replace(microsecond=0)

    if "EndTime" in request.form:
        end_time = request.form['EndTime']
    else:
        end_time = datetime.datetime.now().replace(microsecond=0)

    event = {'user_id': user_id,
             'title': request.form['Title'],
             'description': request.form['Description'],
             'start_time': start_time,
             'end_time': end_time,
             'category_id': request.form['CategoryId'],
             }

    result = event_db.insert_event(event)

    if result is True:
        return {'StatusCode': '200'}
    else:
        return {'StatusCode': '400'}

@app.route('/user/<user_id>/event/<event_id>', methods=['POST'])
def update_event(user_id, event_id):

    if "StartTime" in request.form:
        start_time = request.form['StartTime']
    else:
        start_time = datetime.datetime.now().replace(microsecond=0)

    if "EndTime" in request.form:
        end_time = request.form['EndTime']
    else:
        end_time = datetime.datetime.now().replace(microsecond=0)

    event = {'id': event_id,
             'user_id': user_id,
             'title': request.form['Title'],
             'description': request.form['Description'],
             'start_time': start_time,
             'end_time': end_time,
             'category_id': request.form['CategoryId'],
             }

    result = event_db.update_event(event)

    if result is True:
        return {'StatusCode': '200'}
    else:
        return {'StatusCode': '400'}

if __name__ == '__main__':
    app.run(debug=True)