###************* START *************************************
import tweepy #Library for interacting with Twitter
from tweepy import Stream #For streaming tweets
from tweepy import OAuthHandler # handles Authentication
#from tweepy.streaming import StreamListener #To listen on live tweets
from tweepy import StreamingClient 
from tweepy import API #Twitter API to interact with Twitter data
from os import environ #For keeping secret keys - so that no one sees them on GitHub
import json
import time
###********** Authentication Keys ***********
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
BEARER_TOKEN = environ['Bearer_Token']
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
            blockedUsers = ['995315995840536576','866227142429999105','1476270446370828290','1389686298798174208','1471968770575028233','1476085378209787907','973953546809946112','1018541398683987968','21517400','333430540','1427191265964265482','1104024011707764736','954775174024482816','1552098804303896580','1319400502413676544','857628671976153088','1400837332941611008','1358003167951208448','1541944633','1358676411393978368','1314128451209748480','921673129231077376','1249831869279059968','1197373968530968576','1002292364512292864','1161673407815135238','966073357723750400','244073609','1050436671358025728','1300108986793025542','1344050232506478592','4851188354','924728316','1315551732974317570','1119074582533746688','1447137290095038465','1518937268777779202','1133535860727717891','1423440728034787330','1286081035600629765','1104024011707764736','2943019953','1185827954565304320','4863531979','1329542741726961665','1254439982439202818','1096510105561059328','356151449','3192614035','970037909121314816','293492762','1213376164812607488','2776781889','1413229495746764816','1458568111439892480','1435178496377114627','1089255188878319617','1166343075922415618','1260692428962627594','850117639754088449','1537345857506492417','4872636304','129364320','2316081662','2343534998','1447652109420310533','1289331842076880905','780517716713021440','1448663588097257472','89189819','707744577873059842','1526244399117647872','735572984694476800','1170575543064043520','929894326573895683','1529061381189812226','1111645631175712768','4236288515','1089230731648397313','1522446530065666054','1319146865066233861','1445113530492100617','935711715999735808','1398125508144119812','1619498032550055936','961627558897967112','1418107523559796738','913358844272750592','1626270030001324034','1428935255252160517','1236933295134445568','1586235318973468672','929894326573895683','1451510792529055751','1447137290095038465','1050436671358025728','1325131398773092352','3251043446','1192438921747222529','1609915450439122948','2570245905','1608057244612169729','1658309217902809091']
            blockedUsersInt = [eval(i) for i in blockedUsers]
            userID = int(tweet.author_id)
            blockedID = []
            for user in blockedUsersInt:
                if user == userID:
                    blockedID.append(user)
            if len(blockedID) !=0:
                print("**********************************************")
                print("Oppsssssssssssssssssssssssssss!")
                print("**********************************************")
                return
            
            blocked_words=['dinka','nuer','ethnocide','cheater','Tigray', 'TPLF','genocide','sex','porn','fuck','dog', 'oromo','bokoharam',
            'ugly','horny', 'bitch','penis','vagina','Illuminati', 'pornography','tribes', 'sarmuta',
            'biafra','WarsGenerator','authenticfabric', 'timor','ambazon','Email List',
            'nuer tribe', 'dinka tribe', 'killing','genocide','email list','#SouthSudanEmailList']
            blocked_words_final = []

            for word in blocked_words:
                blocked_words_final.append(word.lower())
            for word in blocked_words:
                blocked_words_final.append(word.upper())
            for word in blocked_words:
                blocked_words_final.append(word.capitalize())

            blockedWordMonitor = []
            for word in blocked_words_final:
                if word in tweet.text:
                    blockedWordMonitor.append(word)
            if len(blockedWordMonitor) != 0:
                print("The word '{}' is blocked".format(blockedWordMonitor))
                return
            else:
                client.retweet(tweet.id)
                print("************************************")
                print("Successfully retweeted a tweet from this id {}. The content of the tweet is {}".format(userID, tweet.text))
                print("************************************")
                time.sleep(25)
    # def on_data(self, data):
    #     tweep_data = json.loads(data)
    #     tweep_username = tweep_data['includes']['users'][0]['username']
    #     self.user_name = tweep_username
    #     print(self.user_name)
    #     return
    def on_errors(self, errors):
        return errors


    
stream = TwitterStream(BEARER_TOKEN, wait_on_rate_limit=True)
rule = tweepy.StreamRule("(South Sudan OR South Sudanese OR #SouthSudanese OR junubin OR junub bot OR junubeen OR #SSOT_tweets OR #SouthSudan OR #SSOT OR @junub_bot OR @mahnzu) (-is:reply)")
stream.add_rules(rule)
stream.filter(tweet_fields=["referenced_tweets"],expansions=["author_id"], user_fields="created_at,description,location,name,protected,username,verified")

#####################################################
##End of file#
###########################