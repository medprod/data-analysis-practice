import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees.rename({'event_day':'day'}, axis=1, inplace=True)
    employees['total_time'] = employees['out_time'] - employees['in_time']
    new_df = employees.groupby(['day', 'emp_id'])['total_time'].sum().reset_index()
    new_df = new_df[['emp_id', 'day', 'total_time']]
    return new_df