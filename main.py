import psycopg2
import pandas as pd
from conn_postgre import con_postgres
from query import customer, mix_table



conn = con_postgres()
cur = conn.cursor()
query = mix_table()
cur.execute(query)
data = cur.fetchall()

df = pd.DataFrame(data, columns=[col[0] for col in cur.description])
df['price'] = df['price'].astype('float')
df['Discount'] = df['price'] * 0.3
df['paymenttype'] = df['paymenttype'].replace('Credit','cicilan')
df.set_index('customername', inplace=True)
df['jumlah_uang'] = df.groupby('customername')['Discount'].sum()
print(df['price'].dtypes)
print(df)
df.to_csv('file_customer.csv', index=True)