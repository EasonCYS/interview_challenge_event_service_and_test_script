# Test Plan

## Funtional Test

### Unit Test
  * Test get, set, create, and delete APIs via pre-defined data with expected results.
  * All fields should exist
  * Value of Category should be in pre-defined set. Follow requirement.
  * Test sort functions using pre-defined input and expected result.
  * Connect real db to verify stored procedure integration.
  * Call tear down functions after all test cases, make sure to clean all test data when finished.
  
### API Test
  * Use Jmeter
  * Use pre-defined test data and expected result
  * Cover all test cases of unit test as possible
  * Prepare data by invoke api first, if unable to do that then insert db directly
  * Clean all test data after finished on test case
  * Authentication and authorization if user need to login first.

#### Test Spec
* Get event list api
  * Success case
    * Happy path: select event lists with several events belonged to user.
    * No sort key, use default (missing key/value, or empty value)
    * No specified order, use default (missing key/value, or empty value).
    * No EndTimeRange, use default (missing key/value, or empty value).
    * Sort by all columns with asc and desc
    * User has no event
    * User has large amount events
    * Boundary test: all columns contain maximum data length.
  * Error Case (should not create event and return pre-defined error then server works normally. No 5xx error.)
    * User not exist
    * Invalid input parameters (sory key, order, EndTimeRange)
    * End time later than current time (return no data or pre-defined error)
    
* Create event api
  * Success case
    * Happy path: create one event with valid data.
    * Concurrency control: create 2 events nearly at the same time, create successfully.
    * No start time, use default
    * No end time, use default.
    * Boundary Test data for all fields.
  * Error Case (should not create event and return pre-defined error then server works normally. No 5xx error.)
    * Invalid referenced data: not exist category id.
    * Missing key for required fields. (no key and no value)
    * Empty value for required fileds. (no value)
    * Invalid fields (data type, data length, etc)
    * Boundary Test Cases: greater than maximum value or less than minimum value.
    * User not exist

* Update event api
  * Success case
    * Happy path: create one event then update with valid data.
    * Concurrency control: update same event nearly at the same time, both update successfully.
    * No start time, use default
    * No end time, use default.
    * Boundary Test data for all fields.
  * Error Case (Should not update event. Return pre-defined error then server works normally. No 5xx error.)
    * Not exist event id
    * User not exist
    * Event not belong to user
    * Invalid referenced data: not exist category id.
    * Missing key for required fields. (no key and no value)
    * Empty value for required fileds. (no value)
    * Invalid fields (data type, data length, etc)
    * Boundary Test Cases: greater than maximum value or less than minimum value.
    * Try to update deleted event.


* Delete event api
  * Success case
    * Happy path: create one event then delete. Get event list should not contain it.
    * Concurrency control: delete same event nearly at the same time, delete successfully and return event not exist for 2nd request.
  * Error Case (Should not update event. Return pre-defined error then server works normally. No 5xx error.)
    * Not exist event id
    * User not exist
    * Event not belong to user
    
## Performance Test

* Leverage the function testing script implemented by jmeter.
* Testing environment should be same as Production environment to avoid any unknown bottleneck.
* Basic Flow (all parameters are configurable in Jmeter):
  1. Phase 1: No traffic for 1-5 minutes, make sure no other influencing factors.
  2. Phase 2: Gradually increase the loading to desired loading, keep for 5-10 minutes, monitor the response
  3. Phase 3: Gradually decrease the lodaing, until no traffic, keep for 1-5 minutes, check if system loading will also recover to initiate state.
* Monitoring indexes:
  * Response time
  * Error rate
  * Throughput
  * Web server resource consumption (CPU, Memory, Disk I/O)
  * DB server resource consumption (CPU, Memory, Disk I/O, deadlocks, lock wait time, etc..)

### Load Test
#### Purpose
Valid system to see if it can work stable under the required traffic.
#### Brief
Send required traffic continously for 10 minutes, monitor system indexes.
#### Detail
* Follow the 3 phases flow
* The maximum traffic is based on the predicted loading of requirement:
  * Concurrent users
  * Different loadings estimation of different api operations
  * Consider the peak and sequential api opereation (such as get -> update -> get)

### Stree Test
#### Purpose
1. To understand the capacity of system.
1. To understand system behaviour when the traffic exceed its capacity.
#### Brief
Gradually increase the traffic of incoming loading, monitor the response time and error rate.
#### Detail
* Follow the 3 phases flow
* Set a extremely high desired traffic
* Monitor the system to see when it will return error response, note the loading
* Set the desired traffic a little higher than the system limitation
* Check if system will recover when loading back to normal (less than the limitation)
* Check system loading (cpu, memory, queue, etc) when loading back to normal.
