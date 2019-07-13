import datetime
import app
import pytest
from db import event_db
from datetime import timedelta

mydb = event_db

start_time = datetime.datetime.now() - timedelta(seconds=60)
start_time = start_time.replace(microsecond=0)
end_time = datetime.datetime.now().replace(microsecond=0)
end_time_range = datetime.datetime.now() - timedelta(hours=48)

event = {'user_id': 1,
        'title': 'pytest test title 3',
        'description': 'test description',
        'start_time': start_time,
        'end_time': end_time,
        'category_id': 1
        }

event_2 = {'user_id': 1,
        'title': 'pytest test title 2',
        'description': 'test description',
        'start_time': start_time - timedelta(seconds=60),
        'end_time': end_time + timedelta(seconds=60),
        'category_id': 1
        }

@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_get_all_event_sort_by_title(client):

    mydb.insert_event(event)
    mydb.insert_event(event_2)

    user_id = event['user_id']
    rv = client.post('/user/' + str(user_id) + '/get_event_list', data=dict(
        SortKey='title',
        Order='desc',
        EndTimeRange=end_time_range))
    json_data = rv.get_json()
    print(json_data)
    assert json_data['Items'][0]['Title'] == 'pytest test title 3'

def test_get_all_event_default(client):
    mydb.insert_event(event)
    mydb.insert_event(event_2)

    user_id = event['user_id']
    rv = client.post('/user/' + str(user_id) + '/get_event_list')
    json_data = rv.get_json()
    assert json_data['Items'][0]['Title'] == 'pytest test title 2'

def test_create_event_by_user_id(client):
    rv = client.post('/user/' + str(event['user_id']) + '/event', data=dict(
        Title = event['title'],
        Description = event['description'],
        StartTime = event['start_time'],
        EndTime=event['end_time'],
        CategoryId = event['category_id']))

    assert b'200' in rv.data
    user_id = event['user_id']

    event_result = mydb.get_events(user_id, 'Id', 'desc', end_time_range)

    assert event_result[0]['UserId'] == event['user_id']
    assert event_result[0]['Title'] == event['title']
    assert event_result[0]['Description'] == event['description']
    assert event_result[0]['StartTime'] == event['start_time']
    assert event_result[0]['EndTime'] == event['end_time']
    assert event_result[0]['CategoryId'] == event['category_id']


def test_update_event(client):
    user_id = event['user_id']
    mydb.insert_event(event)
    event_result_tmp = mydb.get_events(user_id, 'id', 'desc', end_time_range)
    event_id = event_result_tmp[0]['Id']

    event_updated = {'id': event_id,
                     'user_id': 1,
                     'title': 'update pytest test title',
                     'description': 'update test description',
                     'start_time': start_time - timedelta(seconds=60),
                     'end_time': end_time - timedelta(seconds=60),
                     'category_id': 2
                     }

    rv = client.post('/user/' + str(event['user_id']) + '/event/' + str(event_id) , data=dict(
        Title=event_updated['title'],
        Description=event_updated['description'],
        StartTime=event_updated['start_time'],
        EndTime=event_updated['end_time'],
        CategoryId=event_updated['category_id']))

    assert b'200' in rv.data

    event_result = mydb.get_events(user_id, 'id', 'desc', end_time_range)
    assert event_result[0]['UserId'] == event_updated['user_id']
    assert event_result[0]['Title'] == event_updated['title']
    assert event_result[0]['Description'] == event_updated['description']
    assert event_result[0]['StartTime'] == event_updated['start_time']
    assert event_result[0]['EndTime'] == event_updated['end_time']
    assert event_result[0]['CategoryId'] == event_updated['category_id']


def teardown_function():
    user_id = event['user_id']
    mydb.delete_events_by_user_id(user_id)