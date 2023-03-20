###************* START 
import tweepy #Library for interacting with Twitter
from tweepy import Stream #For streaming tweets
from tweepy import OAuthHandler # handles Authentication
#from tweepy.streaming import StreamListener #To listen on live tweets
from tweepy import StreamingClient 
from tweepy import API #Twitter API to interact with Twitter data
import json
from os import environ #For keeping secret keys - so that no one sees them on GitHub
import time
###********** Authentication Keys ***********
# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
# BEARER_TOKEN = environ['Bearer_Token']
CONSUMER_KEY = 'rOITHVw4n3059KmouE3zpJH5w'
CONSUMER_SECRET = 'hJW3y6nE4La8IETYAK2hTyJuzVM8b5xM5GlTksHmcgEsRA0vZ6'
ACCESS_KEY = '1417850839910162432-PYrLWVtbZvkRW3KTTCsIUdlJhsSGf6'
ACCESS_SECRET = 'zHdV7EvDD9S8wbLn46ujm4cMjllfROEZYaINaKPcxamlU'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAGeXRwEAAAAAIUaWqcoFhnf4510kchcZr1JuGYc%3D3moJsI6GPyoe1jQB8WlY7ds0Q3DnSnRbfIncB4CIVhcDu7qLRt'
# client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
ssd_list = ["South Sudan","South Sudanese","#SouthSudanese","junubin","junub bot","junubeen","#SSOT_tweets","#SouthSudan","#SSOT", "@junub_bot","gerald manzu"]

#create a streaming class
class TwitterStream(tweepy.StreamingClient):
    def on_connect(self):
        print("You have successfully connected")
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None: 
            print(tweet.text)
            client.retweet(tweet.id)
            print("Successfully retweeted")
            time.sleep(50)
    
    # def on_data(self, data):
    #     tweep_data = json.loads(data)
    #     tweep_username = tweep_data['includes']['users'][0]['username']
    #     self.user_name = tweep_username
    #     print(self.user_name)
    #     return
  

    def on_errors(self, errors):
        return errors


    
stream = TwitterStream(BEARER_TOKEN, wait_on_rate_limit=True)
rule = tweepy.StreamRule("(South Sudan OR South Sudanese OR #SouthSudanese OR junubin OR junub bot OR junubeen OR #SSOT_tweets OR #SouthSudan OR #SSOT OR @junub_bot OR @mahnzu) (-is:retweet -is:reply)")
stream.add_rules(rule)
stream.filter(tweet_fields=["referenced_tweets"],expansions=["author_id"], user_fields="created_at,description,location,name,protected,username,verified")


