import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].nunique().reset_index()
    orders = orders.loc[orders['order_number']==orders['order_number'].max()][['customer_number']]
    return orders