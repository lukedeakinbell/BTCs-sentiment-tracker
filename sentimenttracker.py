from textblob import TextBlob

# Sample tweet
tweet_text = "Bitcoin is not the future of money."

# Create a TextBlob object
blob = TextBlob(tweet_text)

# Get the sentiment polarity (-1 for negative, 0 for neutral, 1 for positive)
sentiment_polarity = blob.sentiment.polarity

# Classify the sentiment as positive, negative or neutral
if sentiment_polarity > 0:
    sentiment = "positive"
elif sentiment_polarity == 0:
    sentiment = "neutral"
else:
    sentiment = "negative"

print(f"The sentiment of the tweet '{tweet_text}' is {sentiment}.")
