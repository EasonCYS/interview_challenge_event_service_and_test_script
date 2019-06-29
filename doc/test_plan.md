# Test Plan

## Funtional Test

* Unit Test
  * Test get, set, create, and delete APIs via pre-defined data with expected results.
  * All fields should exist
  * Value of Category should be in pre-defined set. Follow requirement.
  * Test sort functions using pre-defined input and expected result.
  * Boundary Test Cases: Data length > maximum; Data length =0 (empty)
  * All sub-functions should write major test functions, such as sorting.
  * No need to connect real db, use local storage instead
  * Create
    * Happy path
    * Missing fields
    * Invalid fields (data type, length, etc)
  * Update Event
    * Happy path
    * Missing fields
    * Broken data
    * Invalid fields (data type, length, etc)
  * Delete Event
    * Happy path
    * Broken data
    * Non-exist events
  
* API Test
  * Use Jmeter
  * Use pre-defined test data and expected result
  * Cover all test cases of unit test as possible
  * Prepare data by invoke api first, if unable to do that then insert db directly
  * Clean all test data after finished on test case
  * Create event api
    * Including same scope of unit test
    * More test cases related to Event DB, such as duplicate, concurrency control, etc
    * Security mechanism (authentication, authorization, etc)
    * Get event list in the end to verify result
  * Update event api
    * Including same scope of unit test
    * More test cases related to Event DB, such as duplicate, concurrency control, etc
    * Security mechanism (authentication, authorization, etc)
    * Get event list in the end to verify result
  * Delete event api
    * Including same scope of unit test
    * More test cases related to Event DB, such as duplicate, concurrency control, etc
    * Security mechanism (authentication, authorization, etc)
    * Get event list in the end to verify result


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
