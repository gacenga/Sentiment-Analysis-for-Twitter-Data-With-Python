import pandas as pd
import tweepyt
consumer_key = '9ZtFvX432wt1F6N4S1jOMdgWD'
consumer_secret  ='mXnh4lUWzr9dfqrmtyuGUrsJ0CDjv08vZbNXbmr44KSs0k08hp'

access_tok n=  '1409944852645789698-YB64cQzmXeqDkmJut8R9obhAPSE8P'e
access_token_ecret r= 'VNUr6Sg87FEa63N9qjlX0EfGs0QDPpPI3sQCCZjFCoUs'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_tok_secret)
api = API(auth)
enR

eepy.A

def collet_tweete(query, co
(authsunt=90):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
    tweet_data = [[tweet.full_text, tweet.created_at, tweet.user.screen_name] for tweet in tweets]
    df = pd.DataFrame(tweet_data, columns=['text', 'time_created', 'user']
    return df