"""
Problem Title: Smart Retail Business Intelligence Dashboard using NumPy and Pandas

Problem Statement:

A multinational retail company maintains its business data in multiple CSV files.

The management wants to generate a complete Business Intelligence Dashboard using both NumPy and Pandas.

Four CSV files are available.

Customer File contains:
Customer ID
Customer Name
City

Product File contains:
Product ID
Product Name
Category
Unit Price

Order File contains:
Order ID
Customer ID
Product ID
Order Date
Quantity

Payment File contains:
Order ID
Payment Amount

The program should perform the following operations.

Step 1:Load all CSV files using Pandas.
Step 2:Merge all datasets into a single DataFrame.
Step 3:Convert Order Date into Datetime format.
Step 4:Create a monthly revenue report using resample().
Step 5:Create a Pivot Table showing category-wise monthly revenue.
Step 6:Using groupby(), display category-wise total revenue.
Step 7:Using loc(),display only Electronics orders.
Step 8:Using iloc(),display the second and third order records.
Step 9:Using NumPy,calculate a 10% bonus revenue for every payment using Vectorization.
Bonus Revenue=Payment Amount × 10%

Step 10:Using NumPy Broadcasting,calculate the Final Revenue.
Final Revenue=Payment Amount + Bonus Revenue

Step 11:Display the highest revenue category.
Step 12:Display the highest spending customer.

Requirements
------------
1. Read four CSV files.
2. Merge multiple DataFrames.
3. Use loc().
4. Use iloc().
5. Use groupby().
6. Use pivot_table().
7. Use pd.to_datetime().
8. Use DatetimeIndex.
9. Use resample().
10. Use NumPy Arrays.
11. Use Vectorization.
12. Use Broadcasting.

Input Files
-----------
customers.csv
products.csv
orders.csv
payments.csv

Output Format
-------------
Complete Business Report
...
Electronics Orders
...
Second and Third Orders
...
Monthly Revenue Report
...
Category-wise Monthly Revenue Pivot Table
...
Category Revenue Report
...
Updated Revenue (10% Bonus)
...
Highest Revenue Category
...
Highest Spending Customer
...

customers.csv
--------------
CustomerID,CustomerName,City
C101,Ravi,Hyderabad
C102,Priya,Chennai
C103,Rahul,Bangalore
C104,Anu,Mumbai
C105,Kiran,Hyderabad


products.csv
-------------
ProductID,ProductName,Category,UnitPrice
P101,Laptop,Electronics,65000
P102,Mobile,Electronics,25000
P103,Shoes,Fashion,2000
P104,Watch,Accessories,3000
P105,Headphones,Electronics,3000

orders.csv
------------
OrderID,CustomerID,ProductID,OrderDate,Quantity
O101,C101,P101,2025-01-05,1
O102,C102,P103,2025-01-15,2
O103,C103,P102,2025-02-02,1
O104,C104,P104,2025-02-18,3
O105,C105,P105,2025-03-10,2

payments.csv
-------------
OrderID,PaymentAmount
O101,65000
O102,4000
O103,25000
O104,9000
O105,6000


case=1
output=
Complete Business Report
O101 Ravi Hyderabad Laptop Electronics 1 65000
O102 Priya Chennai Shoes Fashion 2 4000
O103 Rahul Bangalore Mobile Electronics 1 25000
O104 Anu Mumbai Watch Accessories 3 9000
O105 Kiran Hyderabad Headphones Electronics 2 6000

Electronics Orders
O101 Ravi Laptop 65000
O103 Rahul Mobile 25000
O105 Kiran Headphones 6000

Second and Third Orders
O102 Priya Shoes 4000
O103 Rahul Mobile 25000

Monthly Revenue Report
2025-01 69000
2025-02 34000
2025-03 6000

Category-wise Monthly Revenue Pivot Table

Category 2025-01 2025-02 2025-03
Accessories 0 9000 0
Electronics 65000 25000 6000
Fashion 4000 0 0

Category Revenue Report
Electronics 96000
Accessories 9000
Fashion 4000

Updated Revenue (10% Bonus)
65000 6500.0 71500.0
4000 400.0 4400.0
25000 2500.0 27500.0
9000 900.0 9900.0
6000 600.0 6600.0

Highest Revenue Category
Electronics 96000

Highest Spending Customer
Ravi 65000

"""
import numpy as np
import pandas as pd
customer_df=pd.read_csv("customers.csv")
product_df=pd.read_csv("products.csv")
order_df=pd.read_csv("orders.csv")
payment_df=pd.read_csv("payments.csv")
merge_df1=pd.merge(order_df,product_df,on="ProductID")
merge_df2=pd.merge(merge_df1,payment_df,on="OrderID")
merge_df3=pd.merge(merge_df2,customer_df,on="CustomerID")
final_df=merge_df3.loc[:,["OrderID","CustomerName","City","ProductName","Category","Quantity","PaymentAmount","OrderDate"]].sort_values(by="OrderID")
print("Complete Business Report")
print(final_df.loc[:,["OrderID","CustomerName","City","ProductName","Category","Quantity","PaymentAmount"]].to_string(index=False,header=False))
print("\nElectronics Orders")
print(final_df.loc[final_df["Category"]=="Electronics",["OrderID","CustomerName","ProductName","PaymentAmount"]].to_string(index=False,header=False))
print("\nSecond and Third Orders")
print(final_df.iloc[1:3][["OrderID","CustomerName","ProductName","PaymentAmount"]].to_string(index=False,header=False))
final_df["OrderDate"]=pd.to_datetime(final_df["OrderDate"])
final_df.index=pd.DatetimeIndex(final_df["OrderDate"])
print("\nMonthly Revenue Report")
monthly_revenue=final_df.resample("M")["PaymentAmount"].sum()
monthly_revenue.index=monthly_revenue.index.strftime("%Y-%m")
monthly_revenue.index.name=None
print(monthly_revenue.to_string(header=False))
final_df["Month"]=final_df["OrderDate"].dt.strftime("%Y-%m")
print("\nCategory-wise Monthly Revenue Pivot Table\n")
pivot_df=pd.pivot_table(final_df,values="PaymentAmount",index="Category",columns="Month",aggfunc="sum",fill_value=0)
pivot_df.columns.name=None
pivot_df=pivot_df.reset_index()
print(pivot_df.to_string(index=False))
print("\nCategory Revenue Report")
category_revenue=final_df.groupby("Category")["PaymentAmount"].sum().sort_values(ascending=False)
print(category_revenue.to_string(header=False))
print("\nUpdated Revenue (10% Bonus)")
payment_array=np.array(final_df["PaymentAmount"])
bonus_array=0.1*payment_array
updated_revenue=payment_array+bonus_array
for i in range(len(payment_array)):
    print(f"{payment_array[i]} {bonus_array[i]} {updated_revenue[i]}")
print("\nHighest Revenue Category")
print(category_revenue.idxmax(),category_revenue.max())
print("\nHighest Spending Customer")
customer_spending=final_df.groupby("CustomerName")["PaymentAmount"].sum().sort_values(ascending=False)
print(customer_spending.idxmax(),customer_spending.max())