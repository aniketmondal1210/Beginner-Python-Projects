# Student Records - Menu-Driven Program

## Overview
This task involves implementing a menu-based student record management system. Users can perform various actions including viewing, searching, filtering, adding, and deleting student records. The program will keep running until the user chooses to exit.

## Functional Requirements

### 1. Accept User Input
Prompt the user to choose an action from the following options:
- **View students**
- **Search**
- **Filter**
- **Add**
- **Delete**
- **Exit**

### 2. View Students
- Load and display all student records from the storage (e.g., a file or in-memory structure).

### 3. Search for a Student
- Prompt the user to input a student ID.
- Display the student record if found.
- If no matching student is found, show an error message.

### 4. Filter Students
- Ask the user to filter by either **CGPA** or **Age**.
- Ask for the condition (e.g., `>`, `<`, `=`) and the value.
- Display the list of students matching the condition.

### 5. Delete a Student
- Prompt for the student ID.
- Remove the corresponding student record if found.
- Save the updated student records.

### 6. Exit
- Exit the program cleanly.

### 7. Continuous Execution
- The menu and prompt will repeat until the user selects **Exit**.

## Example Menu Prompt
```
Choose an action:
1. View Students
2. Search
3. Filter
4. Add
5. Delete
6. Exit
Enter choice: 
```

Make sure to handle invalid choices and provide user-friendly messages throughout the interaction.
