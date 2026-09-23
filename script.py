import pandas as pd 
import matplotlib.pyplot as plt
file_path = r"C:\Users\hp\Documents\~a\retail\data\online_retail_II.xlsx"
df = pd.read_excel(file_path)
print(df.columns)
daily_demand = pd.DataFrame(columns=['Date','StockCode','UnitsSold','Revenue'])
df['Date'] = pd.to_datetime(df['InvoiceDate']).dt.date

df['Revenue'] = df['Quantity'] * df['Price']

daily_demand = (
    df[df['Quantity'] > 0]
    .groupby(['Date', 'StockCode'], as_index=False)
    .agg(
        UnitsSold=('Quantity', 'sum'),
        Revenue=('Revenue', 'sum')
    )
)
daily_total = daily_demand.groupby('Date')['UnitsSold'].sum()

daily_total.plot(
    figsize=(12, 5),
    title='Total Daily Units Sold',
    xlabel='Date',
    ylabel='Units Sold'
)
plt.show()