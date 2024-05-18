import pandas as pd
import tweepy

consumer_key = '9ZtFvX432wt1F6N4S1jOMdgWD'
consumer_secret  ='mXnh4lUWzr9dfqrmtyuGUrsJ0CDjv08vZbNXbmr44KSs0k08hp'
access_token=  '1409944852645789698-YB64cQzmXeqDkmJut8R9obhAPSE8P'
access_token_secret = 'VNUr6Sg87FEa63N9qjlX0EfGs0QDPpPI3sQCCZjFCoUs'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = API(auth)

def collect_tweets(query, count=90):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
    tweet_data = [[tweet.full_text, tweet.created_at, tweet.user.screen_name] for tweet in tweets]
    df = pd.DataFrame(tweet_data, columns=['text', 'time_created', 'user'])
    return df
