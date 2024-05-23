import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    newdf = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    newdf.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return newdf