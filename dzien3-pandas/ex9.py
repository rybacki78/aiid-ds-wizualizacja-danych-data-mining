import pandas as pd

data = {
    "Region": ["North", "South", "East", "West"],
    "Product": ["Electronics", "Furniture", "Clothing", "Electronics"],
    "Sales_Channel": ["Online", "Retail", "Online", "Wholesale"],
    "Units_Sold": [120, 80, 200, 150],
    "Revenue": [60.5, 45, 35, 70],
    "Profit": [15.2, 12, 8.5, 20.5],
}

df = pd.DataFrame(
    data,
    columns=["Region", "Product", "Sales_Channel", "Units_Sold", "Revenue", "Profit"],
)

print(df)
df.info()

print(df[df["Profit"] > 13])
