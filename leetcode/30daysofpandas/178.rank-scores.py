import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorteddf = scores.sort_values(by='score', ascending=False)
    sorteddf['rank'] = sorteddf['score'].rank(axis=0, method='dense', ascending=False)
    return sorteddf[['score', 'rank']]