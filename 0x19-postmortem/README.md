![alt text](image.png)


# Postmortem: Resourcify Outage

## Issue Summary
**Duration:** August 25, 2024, 10:00 AM - 11:30 AM (UTC)

**Impact:** Resourcify experienced a significant outage during which 70% of users were unable to access the platform. The remaining 30% encountered slow response times when trying to load resources. The outage affected the core functionalities, including resource submissions, user authentication, and the tech news feed.

**Root Cause:** The root cause was an unoptimized SQL query that led to a database lock, causing a cascading failure across the platform.

## Timeline
- **10:00 AM:** Issue detected by Datadog that reported high latency on the resource API endpoints.
- **10:05 AM:** Initial investigation began by checking the server load and network traffic. It was assumed to be a network issue.
- **10:15 AM:** At the backend, I noticed the database CPU usage was spiking but initially misattributed it to a scheduled database backup.
- **10:30 AM:** Escalated to the database administrator, who identified that an unoptimized SQL query in the resource retrieval function was causing a lock on the database.
- **10:45 AM:** The query was optimized, and the database was restarted to clear the locks.
- **11:00 AM:** The service began recovering, and the platform returned to normal operations by 11:30 AM.

## Root Cause and Resolution
**Root Cause:** The issue was caused by an inefficient SQL query that performed a full table scan every time a user requested a resource. The high volume of simultaneous requests overwhelmed the database, causing it to lock up, which in turn slowed down or completely blocked other queries.

**Resolution:** The query was optimized by adding appropriate indexing to the database table, which significantly reduced the execution time. Additionally, the database was restarted to clear the existing locks, allowing the system to return to normal operation.

## Corrective and Preventative Measures
**Improvements:**
- Enhance query optimization practices during development to prevent similar issues.
- Improve database monitoring to detect and alert on long-running queries.
- Implement rate-limiting to prevent overwhelming the database with too many requests at once.

**Tasks:**
1. **Patch the SQL query:** Modify the existing SQL queries to ensure they are optimized and perform efficiently under load.
2. **Add Database Indexes:** Add indexes to frequently accessed columns in the resource table to speed up query execution.
3. **Implement Rate-Limiting:** Deploy rate-limiting on API endpoints to control the number of requests from users and prevent overload.
4. **Monitor Database Performance:** Set up detailed monitoring on database performance, focusing on query execution times and resource usage.
5. **Review Code for Optimization:** Conduct a full code review focused on identifying and optimizing other potentially inefficient queries and processes.
