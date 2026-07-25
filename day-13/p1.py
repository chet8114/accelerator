## Problem 8: The Comprehensive Memory & Speed Optimization Suite 
"""
Problem Statement:
To round out the foundation sprint, write a diagnostic suite that processes a system telemetry log. 
The script must optimize memory using Pandas downcasting and then offload heavy data processing to 
a Polars Lazy processing graph to keep memory usage minimal.  

The application must execute the following operations:
1.Parse the system memory footprint payload file via Pandas.
2.Downcast the MemoryUsagePct column using pd.to_numeric() to its smallest valid float variant.
3.Feed this optimized Pandas framework structure directly into a Polars Lazy Graph configuration. 
4.Apply a filter tracking records where MemoryUsagePct > 75.0.
5.Execute .collect() to finalize the data structure pipeline and display the results.  

Requirements:
1.Combine Pandas downcast and Polars Lazy APIs (pl.from_pandas().lazy()). 
2.Display matching target optimization lines.

Input File:
------------
system_logs.csv

Output Format:
----------------
Pandas Vector Optimized Type: ...
High Resource Violations Detected:
...

Sample system_logs.csv:
----------------------
HostID,MemoryUsagePct,ContainersCount
H1,55.4,3
H2,89.2,8
H3,76.1,5
H4,43.0,2

Test Case:
----------
case=1
output=
Pandas Vector Optimized Type: float32
High Resource Violations Detected:
H2 89.19999694824219 8
H3 76.0999984741211 5

"""
import pandas as pd
import polars as pl
df=pd.read_csv("system_logs.csv")
df["MemoryUsagePct"]=pd.to_numeric(df["MemoryUsagePct"],downcast="float")
print("Pandas Vector Optimized Type:",df["MemoryUsagePct"].dtype)
print("High Resource Violations Detected:")
lazy_df=pl.from_pandas(df).lazy()
res=(lazy_df.filter(pl.col("MemoryUsagePct")>75.0).collect())
for row in res.iter_rows():
    print(*row)
