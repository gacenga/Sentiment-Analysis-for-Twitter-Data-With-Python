import tweets
import clean_tweets
import sentiment_analysis
import visualize_sentiments
import to_excel

try:
    tweet = tweets.collect_tweets('2023 Toyota Probox Van NHP160V', 20)
    tweet['clean_text'] = tweet['text'].apply(clean_tweets.clean_tweets)
    tweet['sentiment'] = tweet['clean_text'].apply(sentiment_analysis.get_sentiment)

    sent_dist_png, sent_dist_html = visualize_sentiments.sentiment_distribution(tweet)

    tweet['time_created'] = pd.to_datetime(tweet['time_created'])
    tweet.set_index('time_created', inplace=True)
    sentiment_time = tweet['sentiment'].resample('H').value_counts().unstack().fillna(0)

    sent_time_png, sent_time_html = visualize_sentiments.sentiment_timeseries(sentiment_time)
    to_excel.to_excel([sent_dist_png, sent_time_png], [sent_dist_html, sent_time_html])
except Exception as e:
    print(f'An error has occured: {e}')
