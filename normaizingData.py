import pandas as pd
# Simulating data loading
data = pd.DataFrame({"Feature1": range(1, 6), "Feature2": [2, 4, 6, 8, 10]})
print("Dataset Head:\n", data.head())
# Performing basic preprocessing (normalization)
data["Normalized_Feature2"] = data["Feature2"] / max(data["Feature2"])
print("Normalized Data:\n", data)