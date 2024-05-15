import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    newdf = employee.merge(department, how='left', left_on='departmentId', right_on='id')
    newdf = newdf.rename(columns={'name_y': 'Department', 'name_x':'Employee', 'salary':'Salary'})[['Department', 'Employee', 'Salary']]
    return newdf[newdf['Salary'] == newdf.groupby('Department')['Salary'].transform(max)]