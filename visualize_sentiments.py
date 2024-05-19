import matplotlib.pyplot as plt
import seaborn as sns
import to_excel

def sentiment_distribution(dataframe):
    """creates histogram and saves it into an excel file"""
    sns.countplot(x='sentiment', data=dataframe)
    plt.title('sentiment distribution for tweets')
    plt.xlabel('sentiment')
    plt.ylabel('Number of Tweets')
    plot_filename = 'sent_dist.png'
    plt.savefig(plot_filename)
    plt.close()
    to_excel.to_excel(plot_filename, 'E5')

def sentiment_timeseries(sentiment_time):
    """creates time series of sentiment over time and saves it in an excel file"""
    sentiment_time.plot(kind='line', figsize=(12, 6))
    plt.title('Sentiment over Time')
    plt.xlabel('time')
    plt.ylabel('Number of Tweets')
    plot_filename = 'sent_timeseries.png'
    plt.savefig(plot_filename)
    plt.close()
    to_excel.to_excel(plot_filename, 'E20')
    
