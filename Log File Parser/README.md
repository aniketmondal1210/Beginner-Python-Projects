# Log Statistics Functionality

## Overview
Now that keyword-based log searching is in place, we will implement **Log Statistics** to provide users with a summary of the log file.

### Purpose
The `log_statistics()` function will analyze a log file and present:
- The **total number of log entries**.
- The **count of each log level** (INFO, WARNING, ERROR).
- The **most recent log entry** based on appearance in the file.

## Task Requirements
Update the `log_statistics()` function to:

1. **Read all log entries from the log file.**
2. If no logs exist:
   - Output: `"No logs found to analyze."`
3. Otherwise, display:
   - Total number of logs.
   - Count of logs at each level (`INFO`, `WARNING`, `ERROR`).
   - Most recent log entry.

## Expected Output Example
```
Choose an option: 5

--- Log Statistics ---
Total logs: 15
INFO logs: 7
WARNING logs: 5
ERROR logs: 3
Most recent log: 2025-03-31 10:45:12 [WARNING] Low disk space
```

## Notes
- Assume that logs are stored line-by-line in a text file.
- Each log line follows a format such as:
  ```
  2025-03-31 10:45:12 [WARNING] Low disk space
  ```
- The most recent log is the last line in the log file.

Ensure that the `log_statistics()` function reflects these behaviors accurately.
