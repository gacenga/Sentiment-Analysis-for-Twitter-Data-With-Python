import tweets
import clean_tweets
import sentiment_analysis
import visualize_sentiments

tweet = collect_tweets('2023 Toyota Probox Van NHP160V')
tweet['clean_text'] = tweet['text'].apply(clean_tweets)
tweet['sentiment'] = tweet['clean_text'].apply(get_sentiment)

sentiment_distribution(tweet)

tweet['time_created'] = pd.to_datetime(tweet['time_created'])
tweet.set_index('time_created', inplace=True)
sentiment_time = tweet['sentiment'].resample('H').value_counts().unstack().fillna(0)

sentiment_timeseries(sentiment_time)
