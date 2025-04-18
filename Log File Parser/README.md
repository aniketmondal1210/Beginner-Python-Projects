# Log File Parser - Flow

## Overview
This task involves creating a menu-driven **Log File Parser** program that allows users to generate and analyze logs in various ways. The program supports generating new logs, viewing, filtering, searching, and displaying log statistics.

## Functional Flow

### 1. Accept User Input
Prompt the user to choose an action:
- **Generate a log**
- **View logs**
- **Filter logs**
- **Search logs**
- **View log statistics**
- **Exit**

### 2. Generate a Log
- Randomly generate a log entry with:
  - A current timestamp
  - A log level (INFO, WARNING, ERROR)
  - A message
- Append the generated log to the log file.
- Display a confirmation message.

### 3. View All Logs
- Open and read all log entries from the log file.
- Display the entries in the console.
- If no logs exist, display a message like: `"Log file is empty."`

### 4. Filter Logs by Level
- Prompt the user for a log level: `INFO`, `WARNING`, or `ERROR`.
- Read the file and display only the logs that match the selected level.
- If no matching logs are found, show an appropriate message.

### 5. Search Logs by Keyword
- Prompt the user for a keyword.
- Read the log file and search for log lines containing the keyword.
- Display matching logs.
- If no matches are found, display a message indicating so.

### 6. View Log Statistics
- Read the entire log file.
- Count the number of logs for each level:
  - `INFO`
  - `WARNING`
  - `ERROR`
- Display total logs and the count for each level.
- If the file is empty, show an appropriate message.

### 7. Exit
- Gracefully terminate the program.

### 8. Continuous Execution
- The program should display the menu repeatedly and execute the selected functionality until the user chooses to **Exit**.

## Example Menu Prompt
```
Choose an action:
1. Generate a Log
2. View Logs
3. Filter Logs by Level
4. Search Logs by Keyword
5. View Log Statistics
6. Exit
Enter your choice:
