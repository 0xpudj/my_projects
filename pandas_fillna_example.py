import pandas as pd
import numpy as np
# Create a DataFrame with missing values
df = pd.DataFrame({
'Name': ['Alice', 'Bob', np.nan, 'David'],
'Age': [24, np.nan, 22, 32],
'City': ['New York', 'Paris', 'London', np.nan]})
# Fill missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age':df['Age'].mean(), 'City': 'Unknown'})
print(df_filled)