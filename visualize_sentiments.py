import matplotlib.pyplot as plt
import seaborn as sns
import to_excel

def sentiment_distribution(dataframe):
    """creates a histogram for the sentiment distribution and saves it in excel"""
    fig = px.histogram(dataframe, x='sentiment', title='Sentiment Distribution for Tweets')
    plot_filename_png = 'senti_dist.png'
    plot_filename_html = 'senti_dist.html'
    fig.write_image(plot_filename_png)
    fig.write_image(plot_filename_html)
    to_excel.to_excel(plot_filename_png, plot_filename_html)
    
def sentiment_timeseries(sentiment_time):
    """creates a time series for sentiment over time and saves it in excel"""
    fig = go.Figure()
    for sentiment in sentiment_time.columns:
        fig.add_trace(go.Scatter(x=sentiment_time.index, y=sentiment_time[sentiment], mode='lines', name=sentiment))
    fig.update_layout(title='Sentiment over Time', xaxis_title='Time', yaxis_title='Number of Tweets')
    plot_filename_png = 'senti_timeseries.png'
    plot_filename_html = 'senti_timeseries.html'
    fig.write_image(plot_filename_png)
    fig.write_image(plot_filename_html)
    to_excel.to_excel(plot_filename_png, plot_filename_html)
    to_excel.to_excel(plot_filename, 'E20')
    
