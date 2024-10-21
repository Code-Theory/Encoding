import pandas as pd
import numpy as np

data = pd.read_csv('melb_data.csv')

cat_columns = [col for col in data.columns if data[col].dtype == "object" and data[col].nunique() < 10]

print("Categorical columns before encoding:\n")
print(data[cat_columns])

for col in cat_columns:
    unique_values = data[col].unique()
    mapping = {value: idx+1 for idx, value in enumerate(unique_values)}
    data[col] = data[col].map(mapping)

print("\nCategorical columns after encoding:\n")
print(data[cat_columns])