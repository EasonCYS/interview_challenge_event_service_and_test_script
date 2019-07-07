Due to time limitation and considering the purpose of the interview, i decide to write a light-weight test plan and implement sample API test using Jmeter, instead of implement the APIs and Unit tests source code (which are supposedly developed before or with the API source code). 

Assumption
* Only consider user to list her/his own events, not consider cross-users list.
* In most situation, the queries will include a default or specific data range for performance consideration and avoid timeout. For the nature of logs, basically we use start time only. End itme should be optional for only some special events. In order to avoid the overhead of re-index, we don't put it as 3rd level index under user_id -> start_time.


## Test Plan: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/test_plan.md

## Jmeter Script: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/event_list.jmx

## Jmeter Sample Screenshot: 
https://github.com/EasonCYS/migo_test_eason_cheng/blob/master/doc/jmeter%20sample.png
