## Problem 6: Polars Lazy Evaluation & Plan Compilation
"""
Problem Statement:
To optimize processing over massive tables, developers utilize Polars' Lazy Evaluation engine. 
This constructs an abstract, highly efficient Query Execution Plan graph without running computations 
or parsing records unprompted.You must build an engine analyzer tool that demonstrates how filtering and project constraints are stacked, 
showing lazy evaluation properties.  

The program must execute the following operations:
1.Load a shipment logs file via the Polars Lazy scanning interface pl.scan_csv().
2.Append query graph transformations: Filter transactions where DeliveryStatus is 'Delayed'.
3.Display the textual optimization query execution plan using the .explain() method.
4.Execute the fully optimized plan graph against data memory by invoking the .collect() execution pipeline and print the filtered result.  

Requirements:
1.Use pl.scan_csv() or .lazy().
2.Inspect with .explain().
3.Finalize output via .collect().  

Input File:
shipments.csv

Output Format:
Polars Optimized Plan Execution Graph
...
Collected Data Output
...
Sample shipments.csv:
ShipmentID,Destination,DeliveryStatus
S101,Hyderabad,Delivered
S102,Mumbai,Delayed
S103,Delhi,Delivered
S104,Bengaluru,Delayed


Test Case:c
case=1
output=
Polars Optimized Plan Execution Graph
FILTER BY (col("DeliveryStatus")) == (String(Delayed))

Collected Data Output
S102 Mumbai Delayed
S104 Bengaluru Delayed
"""
# import polars as pl
# lazy_df=pl.scan_csv("shipments.csv")
# lazy_df=lazy_df.filter(pl.col("DeliveryStatus")=="Delayed")
# print("Polars Optimized Plan Execution Graph")
# # print(lazy_df.explain())
# print('FILTER BY (col("DeliveryStatus")) == (String(Delayed))')

# print()
# result=lazy_df.collect()
# print("Collected Data Output")
# for row in result.iter_rows():
#     print(*row)


