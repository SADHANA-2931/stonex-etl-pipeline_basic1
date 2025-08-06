import sqlite3
import pandas as pd

# Step 1: Connect to the database
conn = sqlite3.connect('trades.db')

# Step 2: Run a SQL query using Pandas
query = "SELECT * FROM high_value_trades WHERE symbol = 'GOOG'"
df = pd.read_sql_query(query, conn)

# Step 3: Show results
print(df)

# Step 4: Close connection
conn.close()
