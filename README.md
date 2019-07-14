## Event Service ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service

## DB Schema and Stored Procedures ##
* Add indexes for user_id as 1st layer, end_time as 2nd layer (parameter in stored procedure), and other columns as 3rd layers.
* 3 stored procedure for insert, update, select, and delete event.
* For performance consideration, end_time_range is a required input when select events.
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/database

## Unit Test for Event Service ##
https://github.com/EasonCYS/migo_test_eason_cheng/tree/master/migo-event-service/test

## Test Plan: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/test_plan.md

## Jmeter Script: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/event_list.jmx

## Jmeter Sample Screenshot: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/jmeter%20sample.png
