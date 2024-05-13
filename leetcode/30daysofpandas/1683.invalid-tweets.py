import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # tweets['length'] = tweets['content'].str.len()
    return tweets.loc[(tweets['content'].str.len()>15)][['tweet_id']]