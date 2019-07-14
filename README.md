## Event Service ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service

* Only consider user to list her/his own events, not consider cross-users list.
* All the indexes contains "user_id" as 1st layer index and "end_time" as 2nd layer index. 
* The operation of get event list should contain a end time range to accelerate the query. 
** If client didn't input it, the default range would be 24 hours.

## DB Schema and Stored Procedures ##

https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/database

* Add indexes for user_id as 1st layer, end_time as 2nd layer (parameter in stored procedure), and other columns as 3rd layers.
* 4 stored procedure for insert, update, select, and delete event.
* For performance consideration, end_time_range is a required input when select events.


## Unit Test for Event Service ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service/test

## Test Plan: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/test_plan.md

## Jmeter Script: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/event_list.jmx

## Jmeter Sample Screenshot: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/jmeter%20sample.png
