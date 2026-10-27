import pandas as pd
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
#Create a DataFrame from a dictionary
details={"Name":['Alice', 'Bob', 'Charlie'],
         "Age": [25, 30, 35],
         "City": ['New York', 'Los Angeles', 'Chicago']}
task1_data_frame=pd.DataFrame(details)
print(task1_data_frame)

#Add a new column
task1_with_salary=task1_data_frame.copy()
task1_with_salary['Salary']=[70000, 80000, 90000]


#Modify an existing column
task1_older=task1_with_salary.copy()
task1_older['Age']+=1

#Save the DataFrame as a CSV file
newdf=task1_older.copy()
newdf.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
# Read data from a CSV file
task2_employees=pd.read_csv('employees.csv')
print(task2_employees)

# Read data from a JSON file
json_employees=pd.read_json('additional_employees.json')
print(json_employees)

# Combine DataFrames
more_employees=pd.concat([task2_employees,json_employees],ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
#Use the head() method
first_three=more_employees.head(3)
print(first_three)

#Use the tail() method
last_two=more_employees.tail(2)
print(last_two)

#Get the shape of a DataFrame
employee_shape=more_employees.shape
print(employee_shape)

#Use the info() method
print(more_employees.info())

#Task 4: Data Cleaning
dirty_data=pd.read_csv('dirty_data.csv')
print(dirty_data)

clean_data=dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data)

clean_data['Salary'] = clean_data['Salary'].str.strip()
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

clean_data['Hire Date'] = clean_data['Hire Date'].str.strip()
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed')
print(clean_data)

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data)