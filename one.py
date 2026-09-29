import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Price': [200, 500, 150, 800, 350],
    'Quantity_Sold': [50, 20, 100, 15, 60],
    'Discount': [5, 10, 2, 15, 8],
    'Revenue': [10000, 10000, 15000, 12000, 21000]
}

df = pd.DataFrame(data)

print("Original Product DataFrame:")
print(df)

scaler = MinMaxScaler()
cols_to_scale = ['Price', 'Quantity_Sold', 'Discount', 'Revenue']
scaled_values = scaler.fit_transform(df[cols_to_scale])

scaled_df = df.copy()
scaled_df[cols_to_scale] = scaled_values

print("\nTransformed Product DataFrame (Min-Max Scaled):")
print(scaled_df)
