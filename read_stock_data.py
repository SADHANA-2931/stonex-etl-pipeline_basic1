import pandas as pd
df=pd.read_csv('stock_data.csv')
df['trade_value']=df['price'] * df['volume']
high_value_trades=df[df['trade_value']>50000]
print(high_value_trades)

high_value_trades.to_csv('high_value_trades.csv', index=False)