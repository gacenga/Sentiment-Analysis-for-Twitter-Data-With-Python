import tweets
import clean_tweets
import sentiment_analysis
import visualize_sentiments
import to_excel
import tkinter as tk
from tkinter import messagebox

def analyze():
    try:
        keyword = keyword_entry.get().strip()
        tweet = tweets.collect_tweets(keyword, 20)
        tweet['clean_text'] = tweet['text'].apply(clean_tweets.clean_tweets)
        tweet['sentiment'] = tweet['clean_text'].apply(sentiment_analysis.get_sentiment)

        sent_dist_png, sent_dist_html = visualize_sentiments.sentiment_distribution(tweet)

        tweet['time_created'] = pd.to_datetime(tweet['time_created'])
        tweet.set_index('time_created', inplace=True)
        sentiment_time = tweet['sentiment'].resample('H').value_counts().unstack().fillna(0)

        sent_time_png, sent_time_html = visualize_sentiments.sentiment_timeseries(sentiment_time)
        to_excel.to_excel([sent_dist_png, sent_time_png], [sent_dist_html, sent_time_html])
        result_label.config(text="Successfully Analyzed and saved")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

#create main window
root = tk.Tk()
root.title("Sentiment Analysis")

#Create and place keword entry widget
keyword_label = tk.Label(root, text="Enter keyword to search tweets:")
kwyword_label.pack(pady=5)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.pack(pady=5)

#create and place analyze button
analyze_button = tk.Button(root, text="Analyze text", command=analyze)
analyze_button.pack(pady=10)

#create and place result label
result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=10)

#run the application
root.mainloop()
