###************* START ***********************************************************
###**************** Import all the needed **************************************8
###***************** START *******************************************
###******************** Import all the needed ****************************
import tweepy #Library for interacting with Twitter
from tweepy import Stream #For streaming tweets
from tweepy import OAuthHandler # handles Authentication
#from tweepy.streaming import StreamListener #To listen on live tweets
from tweepy import StreamingClient 
from tweepy import API #Twitter API to interact with Twitter data
from tweepy import Cursor #For returning data object to be looped through. Not used though
from os import environ #For keeping secret keys - so that no one sees them on GitHub
import time
###********** Authentication Keys ***********
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
BEARER_TOKEN = environ['Bearer_Token']

client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
if api:
    try:
        print("Successfully authenticated")
    except:
        print("Problem Authenticating")

class MyStream(tweepy.StreamingClient):
    def on_tweet(self,tweet):
        print(tweet.text)
stream = MyStream(BEARER_TOKEN)
rule = tweepy.StreamRule("(#SouthSudan OR #SSOT) (-is:retweet -is:reply)")
stream.add_rules(rule, dry_run=True)
