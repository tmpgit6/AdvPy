import os 
from pathlib import Path
import pandas as pd
os.chdir(Path(__file__).parent)


# Read CSV 
df = pd.read_csv("./my_data.csv")

# Delete unwanted columns
df.drop(columns=["Purchase Address", "Order Date"], inplace=True)

# Delete NANs
df = df.dropna(axis ="rows", how = "any" )

# Delete Repeated Header
df = df.loc[ ~df["Order ID"].str.startswith("Ord")  ]

# Correct Data Types
df["Order ID"] = pd.to_numeric(df["Order ID"])
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])
df["Quantity Ordered"] = pd.to_numeric(df["Price Each"])

# Drop Duplicates
df = df.drop_duplicates()

# Add Brutto Column
df["brutto"] = df["Price Each"] * 1.19

# Save the output File
df.to_csv("./my_data_processed.csv", index = False)

print(df.head())

print(df.dtypes)