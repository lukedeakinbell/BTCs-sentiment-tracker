import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Search for tweets mentioning Bitcoin
query = 'Bitcoin'
tweets = api.search(q=query, lang='en', count=100)

# Print the text of each tweet
for tweet in tweets:
    print(tweet.text)
