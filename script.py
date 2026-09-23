import pandas as pd 
file_path = r"C:\Users\hp\Documents\~a\retail\data\online_retail_II.xlsx"
df = pd.read_excel(file_path)
print(df.head())
print(df.info())