import tweepy

# Set up your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define your search query and the number of tweets you want to retrieve
search_query = "bitcoin OR BTC"
num_tweets = 100

# Collect tweets using the search query
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_query,
                       lang="en",
                       tweet_mode="extended").items(num_tweets)

# Print the text of each tweet
for tweet in tweets:
    print(tweet.full_text)
