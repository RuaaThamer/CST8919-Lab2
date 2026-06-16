# CST8919 Lab 2: Web App with Threat Detection using Azure Monitor and KQL

## Project Description
As part of a Cloud Security Engineering assignment, this repository hosts a simple Python Flask web application deployed to Azure App Service. The application logs user authentication attempts to standard output, allowing Azure Monitor to ingest and route the data (`AppServiceConsoleLogs`) to a Log Analytics Workspace. A custom Kusto Query Language (KQL) alert monitors these logs to automatically flag brute-force attack indicators.

---

## What I Learned
* Configured real-time diagnostic stream telemetry forwarding from an enterprise Azure Web App platform into a central Azure Log Analytics Workspace.
* Authored custom Kusto Query Language (KQL) string evaluations to isolate internal application logic messaging.
* Constructed fully automated metric threshold alert rules inside Azure Monitor using custom action notification groups.

---

## Challenges Faced
* **Azure Logging Ingestion Delay:** Telemetry logs experience a standard 5-to-10 minute buffer delay from application runtime execution to central ingestion, requiring patient validation intervals.
* **Alert Frequency Adjustments:** Due to specific regional optimization constraints in Azure Monitor, the evaluation frequency had to be adjusted from 1 minute to 5 minutes to bypass optimization errors while maintaining functionality.
* **Column Mapping Quirks:** Encountered a syntax error matching standard documentation strings until isolating the precise `ResultDescription` string payload structural mapping requirement.

---

## Improving Detection Logic in a Real-World Scenario
While a flat count check (greater than 5 failed attempts) works as a proof-of-concept, production security environments should be enhanced with:
1. **Dimension Splitting by IP Address:** Evaluating attempts strictly grouped by `ClientIP` or source destination to avoid catching multiple unrelated distributed users experiencing login friction.
2. **Dynamic Baseline Monitoring:** Utilizing Azure ML built-in dynamic threshold options instead of hardcoded static values to catch anomalous behavioral standard deviations.
3. **Geo-Velocity Checks:** Correlating tracking fields with identity access management streams to trigger high-priority actions on impossible travel alerts.

---

AppServiceConsoleLogs
| where ResultDescription contains "Failed login attempt for user"
| project TimeGenerated, Result=ResultDescription
| order by TimeGenerated desc

### Explanation:
* **`AppServiceConsoleLogs`**: References the explicit log table receiving standard input (`stdout`) streams from our Flask application container.
* **`where ResultDescription contains "..."`**: Performs a localized string filter parsing for failed application strings to isolate brute-force traffic.
* **`project`**: Isolates relevant workspace columns (`TimeGenerated` and `Result`) for cleaner log visualization.
* **`order by`**: Organizes data cleanly based on temporal sequencing so that the newest incidents always float to the top of the security queue.

---

## Submission Links

* **YouTube Video Demo:** [INSERT_YOUR_YOUTUBE_LINK_HERE]
