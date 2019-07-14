## Event Service ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service

* 4 APIs for user to get, create, update, and delete her/his own event(s).
* All the indexes for event table contains "user_id" as 1st layer index and "end_time" as 2nd layer index. 
* The operation of get event list should contain a EndTimeRange to accelerate the query. 
  * If client didn't input it, the default range would be 24 hours ago.
  
### Get event list: POST /user/<user_id>/get_event_list

Path parameter
* <user_id>: user id

Form data parameter
* SortKey: (Optional) Column used to be sorted. 
  * Column can be: [ id | user_id | title | description | start_time | end_time | category_id ]
  * Default: id
* Order: (Optional) sort order.
  * Can be: [ asc | desc ]
  * Default: desc
* EndTimeRange: (Optional) The earliest event end time for the returned list, to prevent client query all the events.
  * Default: 24 hours ago
  
### Create Event: POST /user/<user_id>/event

Path parameter
* <user_id>: user id

Form data parameter
* Title: (Required)
* Description: (Required)
* StartTime: (Optional)
  * Default: current time
* EndTime: (Optional)
  * Default: current time
* CategoryId: (Required)

### Update Event: POST /user/<user_id>/event/<event_id>

Path parameter
* <user_id>: user id
* <event_id>: event id

Form data parameter
* Title: (Required)
* Description: (Required)
* StartTime: (Optional)
  * Default: current time
* EndTime: (Optional)
  * Default: current time
* CategoryId: (Required)

### Delete Event: DELETE /user/<user_id>/event/<event_id>
Path parameter
* <user_id>: user id
* <event_id>: event id

## DB Schema and Stored Procedures ##

https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/database

* Add indexes for user_id as 1st layer, end_time as 2nd layer (parameter in stored procedure), and other columns as 3rd layers.
* 4 stored procedures for insert, update, select, and delete event.
* For performance consideration, end_time_range is a required input for select events stored procedure.


## Unit Test ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service/test

* The structure is the same as the source code of service app.
* use ```pytest``` for both web app and db model test, ```pytest test/test_app.py``` for web app, or ```pytest test/db/test_event_db.py``` for db model.

## Test Plan & Test Spec: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/test_plan.md

## Jmeter Script: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/event_list.jmx

## Jmeter Sample Screenshot: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/jmeter%20sample.png
