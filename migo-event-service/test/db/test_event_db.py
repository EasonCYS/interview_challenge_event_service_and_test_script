import datetime
from datetime import timedelta
from db import event_db

mydb = event_db

start_time = datetime.datetime.now() - timedelta(seconds=60)
start_time = start_time.replace(microsecond=0)
end_time = datetime.datetime.now().replace(microsecond=0)
end_time_range = datetime.datetime.now() - timedelta(hours=24)

event = {'user_id': 1,
        'title': 'pytest test title 1',
        'description': 'test description',
        'start_time': start_time,
        'end_time': end_time,
        'category_id': 1
        }


def test_insert_event():
    assert mydb.insert_event(event) == True


def test_update_event():
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

    mydb.update_event(event_updated)

    event_result = mydb.get_events(user_id, 'Id', 'desc', end_time_range)
    assert event_result[0]['UserId'] == event_updated['user_id']
    assert event_result[0]['Title'] == event_updated['title']
    assert event_result[0]['Description'] == event_updated['description']
    assert event_result[0]['StartTime'] == event_updated['start_time']
    assert event_result[0]['EndTime'] == event_updated['end_time']
    assert event_result[0]['CategoryId'] == event_updated['category_id']


def test_get_events():
    mydb.insert_event(event)
    user_id = event['user_id']
    event_result = mydb.get_events(user_id, 'Id', 'desc', end_time_range)
    assert event_result[0]['UserId'] == event['user_id']
    assert event_result[0]['Title'] == event['title']
    assert event_result[0]['Description'] == event['description']
    assert event_result[0]['StartTime'] == event['start_time']
    assert event_result[0]['EndTime'] == event['end_time']
    assert event_result[0]['CategoryId'] == event['category_id']


def test_delete_events():
    user_id = event['user_id']
    mydb.insert_event(event)

    event_result_tmp = mydb.get_events(user_id, 'id', 'desc', end_time_range)
    event_id = event_result_tmp[0]['Id']

    mydb.delete_event(user_id, event_id)
    event_result = mydb.get_events(user_id, 'Id', 'desc', end_time_range)
    assert len(event_result) == 0


def teardown_function():
    user_id = event['user_id']
    mydb.delete_events_by_user_id(user_id)