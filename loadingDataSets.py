import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Viewing data
print("First 5 rows:\n", df.head())
print("\nSummary Info:\n")
df.info()