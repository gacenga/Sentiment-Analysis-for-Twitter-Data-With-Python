import pandas as pd
import tweepy

def collect_tweets(query, count=90):
    """collects tweets from x.com based on specified query"""
    try:
        consumer_key = 'your consumer key'
        consumer_secret = 'your consumer secret api key'
        access_token = 'your access token'
        access_token_secret = 'your secret access token'
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
        tweet_data = [[tweet.full_text, tweet.created_at, tweet.user.screen_name] for tweet in tweets]
        df = pd.DataFrame(tweet_data, columns=['text', 'time_created', 'user'])
        return df
    except Exception as e:
        print(f'An error has occured: {e}')
