"""
Problem Title:
Smart Student Marks Reshaping System using Pandas

Problem Statement:

A university maintains student semester marks in a CSV file.

Initially, the marks are stored in wide format where
each subject is represented as a separate column.

The examination branch wants to convert the data into
long format for analysis and then reconstruct the
original table.

Each student record contains:

Student ID
Student Name
Math
Science
English

The program should perform the following operations.

Step 1:Load the student dataset using Pandas.

Step 2:Display the complete student dataset.

Step 3:Using melt(),convert the dataset from wide format into long format.
The long format should contain:
Student ID
Student Name
Subject
Marks

Step 4:Using pivot(),convert the long format back into the original wide format.

Step 5:Display the reconstructed dataset.

Requirements
------------
1. Read students.csv.
2. Create a Pandas DataFrame.
3. Use melt().
4. Use pivot().
5. Display both long and wide formats.

Input File
----------
students.csv

Output Format
-------------
Original Student Dataset
...
Long Format Dataset
...
Reconstructed Dataset
...

Sample students.csv
-------------------
StudentID,StudentName,Math,Science,English
S101,Ravi,90,85,88
S102,Priya,78,92,81
S103,Rahul,88,79,91

case=1
output=
Original Student Dataset
S101 Ravi 90 85 88
S102 Priya 78 92 81
S103 Rahul 88 79 91

Long Format Dataset
S101 Ravi Math 90
S102 Priya Math 78
S103 Rahul Math 88
S101 Ravi Science 85
S102 Priya Science 92
S103 Rahul Science 79
S101 Ravi English 88
S102 Priya English 81
S103 Rahul English 91

Reconstructed Dataset
S101 Ravi 90 85 88
S102 Priya 78 92 81
S103 Rahul 88 79 91
"""

import pandas as pd
data=pd.read_csv("students.csv")
print("Original Student Dataset")
print(data.to_string(index=False,header=False))
print("\nLong Format dataset")
lon=pd.melt(data,id_vars=["StudentID","StudentName"],value_vars=["Math","Science","English"],var_name="Subject",value_name="Marks")
print(lon.to_string(index=False,header=False))
print("\nReconstructed Dataset")
re=lon.pivot(index=["StudentID","StudentName"],columns="Subject",values="Marks")
re=re.reset_index(level="StudentName")
re=re[["StudentName","Math","Science","English"]]
re.index.name=None
print(re.to_string(header=False))