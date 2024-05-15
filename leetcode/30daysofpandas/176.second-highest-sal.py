import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorteddf = employee.sort_values(by='salary', ascending=False)
    unique_vals = sorteddf['salary'].drop_duplicates()

    if len(unique_vals) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    secnd_highest = unique_vals.iloc[1]
    return pd.DataFrame({'SecondHighestSalary':[secnd_highest]})