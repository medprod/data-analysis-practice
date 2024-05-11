import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    newdf = views.loc[views['author_id']==views['viewer_id']]
    res = newdf[['author_id']].rename(columns={'author_id':'id'})
    res = (res.drop_duplicates(subset='id')).sort_values(by='id')
    # res = res.sort_values(by='id')
    return res