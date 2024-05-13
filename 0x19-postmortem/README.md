# Postmortem: Application Performance Issues After pushing new feature to production server.

![Working pressure](https://pbs.twimg.com/media/GNZ6OcHWUAAQ__r?format=jpg&name=medium)

## Issue Summary:

![Issue Summary](https://pbs.twimg.com/media/GNZ6OeFWYAAoXyY?format=jpg&name=medium)

- **Duration:** The outage occurred from 10:00 AM to 1:00 PM on Jan 10th, 2024 (CAT).
- **Impact:** The performance degradation affected the responsiveness of our Django-based application, leading to a 40% increase in response times for users accessing certain features.
- **Root Cause:** The primary cause was identified as inefficient database queries, leading to high CPU usage on the database server.



## Timeline:
- **10:00 AM:** Issue detected by monitoring alerts indicating a spike in response times.
- **10:15 AM:** Engineering team notified and began investigation.
- **10:30 AM:** Initial assumption focused on network congestion due to recent updates.
- **10:45 AM:** Misleading investigation pursued into frontend caching mechanisms.
- **11:00 AM:** Incident escalated to the database administration team for further analysis.
- **12:00 PM:** Root cause identified as inefficient database queries leading to high CPU load.
- **1:00 PM:** Incident resolved by optimizing database queries and implementing caching mechanisms.

## Root Cause and Resolution:
- **Root Cause:** The root cause of the performance degradation was inefficient database queries, specifically related to complex joins and lack of indexing.
- **Resolution:** The issue was resolved by optimizing the problematic queries, introducing proper indexing, and implementing caching mechanisms to reduce the load on the database server.

![root cause of issues](https://pbs.twimg.com/media/GNZ-qrBXcAIBBoI?format=png&name=large)

## Corrective and Preventative Measures:
- **Improvements/Fixes:**
  - Review and optimize all critical database queries for efficiency.
  - Implement comprehensive indexing strategy to improve query performance.
  - Enhance monitoring and alerting systems to detect performance issues proactively.
- **Tasks to Address the Issue:**
  1. Conduct a thorough review of all database queries and identify optimization opportunities.
  2. Implement indexing on frequently accessed tables to improve query execution times.
  3. Introduce caching mechanisms at the application level to reduce reliance on database queries for certain operations.
  4. Enhance monitoring systems to detect performance anomalies early and trigger alerts for timely intervention.
  5. Conduct regular performance audits to identify and address any emerging bottlenecks before they impact user experience.

  ![rectification mechanism](https://pbs.twimg.com/media/GNZ-qrDXwAA_OzH?format=png&name=large)


## Conclusion:
In conclusion, the performance degradation experienced in our Django application was primarily attributed to inefficient database queries. Through timely detection, rigorous investigation, and targeted optimization efforts, we were able to restore normal functionality and implement measures to prevent similar issues in the future. By prioritizing proactive monitoring and continuous optimization, we aim to ensure a consistently high level of performance and reliability for our users.

