import csv
import statistics

def load_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # Initialize an empty list to store data
            data_list = [] 
            
            for row in reader:
                data_list.append(row)
        
        print("CSV file loaded successfully!")
        return data_list
    except:
        print(" Error loading CSV file.")
        return None
    
# -----------------------------------------------------------
def sort_data(data):
    if not data:
        print(" No data available.")
        return

    column = input("Enter column name to sort by: ")
    
    if column not in data[0]:
        print(" Invalid column name!")
        return

    sorted_data = sorted(data, key=lambda x : x[column])

    print("\n Sorted Data:")
    display_info(sorted_data)
# -----------------------------------------------------------

def display_info(data):
    if not data:
        print("No data available.")
        return

    print("\nInformation:")
    print(f"Total Rows: {len(data)}")
    print("Columns:", *data[0].keys(), "\n")
    headers = list(data[0].keys())

    print("Data:")
    for x in headers:
        print(x + "  ", end="")
    print()
    for i in range(len(data)):
        for col in headers:
            print(data[i][col] + "  ", end="")
        print()

def basic_statistics(data):
    if not data:
        print("No data available.")
        return

    print("\n Basic Statistics:")
    
    columns = list(data[0].keys())
    for column in columns:
        try:
            values = []
            for row in data:
                if row[column]: 
                    values.append(float(row[column])) 
            if values: 
                print(f"\n Column: {column}")
                print(f"   Total Non-Null Values: {len(values)}")
                print(f"   Mean (Average): {statistics.mean(values):.2f}")
                print(f"   Minimum Value: {min(values)}")
                print(f"   Maximum Value: {max(values)}")
                print(f"   Median (50%): {statistics.median(values):.2f}")
                if len(values) > 1:
                    print(f"   Standard Deviation: {statistics.stdev(values):.2f}")
                else:
                    print("   Std Dev: N/A")
        except:
            continue 

def filter_data(data):
    if not data:
        print(" No data available.")
        return

    column = input("Enter column name to filter: ")
    
    if column not in data[0]:
        print(" Invalid column name!")
        return

    value = input(f"Enter value to filter by ({column}): ")

    filtered_data = []
    for i in range(len(data)):  
        if data[i][column] == value: 
            filtered_data.append(data[i]) 

    if not filtered_data:
        print("No matching records found.")
    else:
        print("\n Filtered Data:")
        display_info(filtered_data)


if __name__ == "__main__":
    print("Welcome to CSV Data Analyzer!\n")
    file_path = input("Enter CSV file name (data.csv): ")
    data = load_csv(file_path)

    if data is None:
        exit(1)

    while True:
        print("\nCSV Data Analyzer:")
        print("1. Display Data Info")
        print("2. Show Basic Statistics")
        print("3. Filter Data")
        print("4. Sort Data")
        print("5. Exit")
        choice = int(input("Choose an option: "))

        if choice ==  1:
            display_info(data)
        elif choice == 2:
            basic_statistics(data)
        elif choice == 3:
            filter_data(data)
        elif choice == 4:
            sort_data(data)
        elif choice == 5:
            print(" Exiting...")
            break
        else:
            print(" Invalid choice. Try again!")
