Design
* Only consider user to list her/his own events, not consider cross-users list.
* All the indexes contains "user_id" as 1st layer index and "end_time" as 2nd layer index. The operation of get event list should contain a end time range to accelerate the query. If client didn't input it, the default range would be 24 hours.
