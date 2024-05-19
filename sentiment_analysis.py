from textblob import TextBlob

def get_sentiment(text):
    """gets sentiment from text"""
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'negative'
    
