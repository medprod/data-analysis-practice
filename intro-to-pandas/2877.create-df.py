import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    name = ['student_id', 'age']
    df = pd.DataFrame(student_data, columns=name)
    return df