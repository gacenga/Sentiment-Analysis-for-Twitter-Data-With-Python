import matplotlib.pyplot as plt
import seaborn as sns

def sentiment_distribution(dataframe):
    sns.countplot(x='sentiment', data=dataframe)
    plt.title('sentiment distribution for tweets')
    plt.xlabel('sentiment')
    plt.ylabel('Number of Tweets')
    plt.show()

def sentiment_timeseries(sentiment_time):
    sentiment_time.plot(kind='line', figsize=(12, 6))
    plt.title('Sentiment over Time')
    plt.xlabel('time')
    plt.ylabel('Number of Tweets')
    plt.show()
    