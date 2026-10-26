import traceback
import csv
import os
import custom_module
from datetime import datetime

# Task 2 
def read_employees():
    empdict={}
    rows=[]
    firstrow=True
    try:
        with open('../csv/employees.csv','r') as file:
            reader=csv.reader(file)
            for record in reader:
                if firstrow:
                    empdict['fields'] = record
                    firstrow=False
                else:
                    rows.append(record)
            empdict['rows'] = rows
            return empdict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees=read_employees()
# print(employees)


# Task 3
def column_index(col_name):
    return employees['fields'].index(col_name)

employee_id_column=column_index('employee_id')

# Task 4
def first_name(row_number):
    col_idx=column_index('first_name')
    return employees['rows'][row_number][col_idx]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches=list(filter(lambda row:int(row[employee_id_column]) == employee_id ,employees['rows']))
    return matches
        
# Task 7
def sort_by_last_name():
    employees['rows'].sort(key=(lambda row:row[column_index('last_name')]))
    return employees['rows'] 
sort_by_last_name()
# print(employees)

# Task 8
def employee_dict(row):
    emp_dict=dict(zip(employees['fields'][1:],row[1:]))
    return emp_dict
# print(employee_dict(employees['rows'][0]))

# Task 9
def all_employees_dict():
    all_dict={}
    for i in range(len(employees['rows'])):
        all_dict[employees['rows'][i][0]]=employee_dict(employees['rows'][i])
    return all_dict
print(all_employees_dict())

# Task 10
def get_this_value():
    return os.getenv('THISVALUE')

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
new_string=set_that_secret('New String Secret')
# print(custom_module.secret)

# Task 12
def open_file(path,minutes):
    rows=[]
    firstRow=True
    with open(path,'r')as file:
        reader=csv.reader(file)
        for line in reader:
            if firstRow:
                minutes['fields']=line
                firstRow=False
            else: 
                rows.append(tuple(line))
        minutes['rows']=rows
        return minutes
def read_minutes():
    minutes1_dict={}
    minutes2_dict={}
    try:
        open_file('../csv/minutes1.csv',minutes1_dict)
        open_file('../csv/minutes2.csv',minutes2_dict)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")      
    
    return minutes1_dict,minutes2_dict
minutes1, minutes2 = read_minutes()
# print(minutes1, minutes2)

# Task 13
def create_minutes_set():
    min_set=set()
    min_set=set(minutes1['rows'])|set(minutes2['rows'])
    return min_set 
minutes_set=create_minutes_set()
print (minutes_set)

# Task 14
def create_minutes_list():
    minute_list=list(minutes_set)
    mlist=list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),minute_list))
    return mlist
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    new_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerows(new_list)
    return new_list