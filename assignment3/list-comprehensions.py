# Task 3
import csv
try:
    with open('../csv/employees.csv','r') as file:
        records=csv.reader(file)
        next(records)
        list_of_records=[record[1]+' '+record[2] for record in records]
        elist=[ename for ename in list_of_records if 'e' in ename.lower()]
        print(elist)
except Exception as e:
    print(e)

