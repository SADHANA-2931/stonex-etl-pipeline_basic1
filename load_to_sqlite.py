import pandas as pd
import sqlite3
df=pd.read_csv('high_value_trades.csv')
conn=sqlite3.connect('trades.db')
df.to_sql('high_value_trades',conn, if_exists='replace', index=False)
conn.close()
print("Data successfully saved to database!")