"""
Problem Title: Smart Employee Data Analyzer using Pandas

Problem Statement:

A software company maintains employee details in a CSV file.

The HR department wants to analyze employee information
using the Pandas DataFrame.

Each employee record contains:

Employee ID
Employee Name
Department
Salary
Experience

The program should perform the following operations.

Step 1

Load the employee dataset using Pandas.

Step 2

Display the complete employee dataset.

Step 3

Using loc[],
display all employees belonging to the
Development department.

Step 4

Using iloc[],
display the second and third employee records.

Step 5

Using groupby(),
display the average salary of each department.

Requirements
------------

1. Read employee data from CSV.
2. Create a Pandas DataFrame.
3. Use loc[].
4. Use iloc[].
5. Use groupby().
6. Display average department salary.

Input File
----------

employees.csv

Output Format
-------------

Employee Dataset

...

Development Employees

...

Second and Third Employees

...

Average Salary Department Wise

...

Sample employees.csv
---------------------------

EmployeeID,EmployeeName,Department,Salary,Experience
E101,Ravi,Development,60000,3
E102,Priya,Testing,50000,2
E103,Rahul,Development,70000,5
E104,Anu,HR,45000,4
E105,Kiran,Testing,55000,3



Employee Dataset

  EmployeeID EmployeeName   Department Salary Experience
0 E101 Ravi Development 60000 3
1 E102 Priya Testing 50000 2
2 E103 Rahul Development 70000 5
3 E104 Anu HR 45000 4
4 E105 Kiran Testing 55000 3


Development Employees

  EmployeeID EmployeeName Department Salary Experience
0 E101 Ravi Development 60000 3
2 E103 Rahul Development 70000 5


Second and Third Employees

  EmployeeID EmployeeName Department Salary Experience
1 E102 Priya Testing 50000 2
2 E103 Rahul Development 70000 5


Average Salary Department Wise

Department
Development    65000.0
HR             45000.0
Testing        52500.0
"""
import numpy as np
import pandas as pd
print("Employee Dataset")
print()
df=pd.read_csv("employees.csv")
print(df.to_string())
print()
print()
print("Development Employees")
print()
dev_emp=df.loc[df["Department"]=="Development"]
print(dev_emp.to_string())
print()
print()
print("Second and Third Employees")
print()
s_t=df.iloc[1:3]
print(s_t.to_string())
print()
print()
print("Average Salary Department Wise")
print()
df["Salary"]=df["Salary"].astype(float)
avg=df.groupby("Department")["Salary"].mean()
print(avg)