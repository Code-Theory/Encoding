import pandas as pd
import numpy as np

data = pd.read_csv('melb_data.csv')

cat_columns = [column for column in data.columns if data[column].dtype == 'object' and data[column].nunique() < 10]

print("\nBefore one-hot encoding:\n")
print(data[cat_columns])


    
data_encoded = pd.get_dummies(data, columns=cat_columns, prefix=cat_columns)

data_encoded = data_encoded.replace({True: 1, False: 0})

print("\nAfter one-hot encoding:\n")
print(data_encoded)

