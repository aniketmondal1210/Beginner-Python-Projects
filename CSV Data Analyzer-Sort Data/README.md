# Great going so far.

# Now in this component, we'll implement the sort_data() function to give users the ability to organize their CSV data alphabetically or numerically by any column they choose.

# New Concept - Sorting using key parameter

# The key parameter is an optional argument that allows us to customize the sort order.

# ```python
# a = [
#     {"name": "Alice", "age": 32},
#     {"name": "Bob", "age": 42},
#     {"name": "Eve", "age": 22}
# ]
# # Use sorted() to sort the list 'a' based on the 'age' key
# # sorted() returns a new list with dictionaries sorted by the 'age'
# b = sorted(a, key=lambda x: x['age'])
# print(b)
# # Output:
# # [{'name': 'Eve', 'age': 22}, {'name': 'Alice', 'age': 32}, {'name': 'Bob', 'age': 42}]
# ```

# Explanation: `key=lambda x: x['age']` specifies that the sorting should be done using the ‘age’ value from each dictionary

---

# Task

# Complete the `sort_data()` function to meet the following requirements:

## ✅ Handle Empty Data:

# If input data is empty, display:

# ```
# No data available.
# ```

# Immediately return from the function

## ✅ Prompt the user to:

# Select a column from the available dataset

# If the column doesn’t exist - Display:

# ```
# Invalid column name!
# ```

# Exit the function

## ✅ Sorting Logic:

# - Sort the data in ascending order based on a selected column
# - Preserve original data (create a new sorted list)

## ✅ Display Results:

# - Display sorted data using `display_info()` function

---

## ✅ Expected Output

```plaintext
Choose an option: 4
Enter column name to sort by: Age

 Sorted Data:

Information:
Total Rows: 6
Columns: Name Age Dept Salary 

Data:
Name  Age  Dept  Salary  
Alice  25  HR  50000  
Mohan  27  HR  80000  
Bob  30  IT  60000  
Qais  31  IT  62000  
Umar  36  Finance  72000  
Anuj  40  IT  80000  
