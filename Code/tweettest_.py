# coding=<utf-8>
import tweepy

consumer_key = "Enter the consumer_key"
consumer_secret = "Enter the consumer_secret"
access_key = "Enter the access_key"
access_secret = "Enter the access_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
alltweets=tweepy.Cursor(api.search,q='Tenet').items(1)
for tweet in alltweets:
	print(tweet)
