## Problem 4: Hybrid Strategy: Chunked Processing with In-Flight Downcasting 
"""
Problem Statement:
Your production infrastructure requires processing a massive metrics export 
file under strict 5 GB layout constraints. 
You cannot hold uncompressed objects or entire segments in memory. 
You must integrate a chunking strategy with  real-time numeric optimization on 
each slice before appending it to global counters.

The program must execute the following operations:
--------------------------------------------------
Stream metric records in slices of 2 rows at a time.
For each incoming slice, downcast the MetricValue to its minimal valid numeric memory layout.
Compute and print out the localized safe peak memory overhead of that chunk's MetricValue slice.
Aggregate the global absolute maximum value observed across the entire stream.

Requirements:
-------------
Combine chunksize and pd.to_numeric(..., downcast='float').
Track a rolling global scalar.

Input File:
-------------
metrics.csv

Output Format:
-------------
Chunk Processed - Overhead: ... Bytes
...
Global Peak Metric Observed: ...


Sample metrics.csv:
-------------
Timestamp,MetricName,MetricValue
16112101,CPU_Usage,88.50
16112102,CPU_Usage,92.10
16112103,CPU_Usage,45.00
16112104,CPU_Usage,71.25

Test Case:
-------------
case=1
output=
Chunk Processed - Overhead: 8 Bytes                                             
Chunk Processed - Overhead: 8 Bytes                                             
                                                                                
Global Peak Metric Observed: 92.0999984741211  

"""
import pandas as pd
global_max=float("-inf")
for chunk in pd.read_csv("metrics.csv",chunksize=2):
    chunk["MetricValue"]=pd.to_numeric(chunk["MetricValue"],downcast="float")
    overhead=chunk["MetricValue"].memory_usage(index=False)
    print(f"Chunk Processed - Overhead: {overhead} Bytes")
    chunk_max=chunk["MetricValue"].max()
    if chunk_max>global_max:
        global_max=chunk_max
        
print("\nGlobal Peak Metric Observed:",global_max)
