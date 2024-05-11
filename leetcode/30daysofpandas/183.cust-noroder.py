import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    newdf = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    mask = newdf['customerId'].isna()
    res = newdf[mask]
    res = res[['name']].rename(columns={'name':'Customers'})
    return res