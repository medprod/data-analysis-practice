import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorteddf = employee.sort_values(by='salary', ascending=False)
    unique_sal = sorteddf['salary'].drop_duplicates()

    if N>len(unique_sal) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    nth_highest = unique_sal.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})

     