###********** START **********
###********** START **********
###********** START **********
###********** Import all the needed **********
import tweepy #Library for interacting with Twitter
from tweepy import Stream #For streaming tweets
from tweepy import OAuthHandler # handles Authentication
from tweepy.streaming import StreamListener #To listen on live tweets
from tweepy import API #Twitter API to interact with Twitter data
from tweepy import Cursor #For returning data object to be looped through. Not used though
from os import environ #For keeping secret keys - so that no one sees them on GitHub
import time

###********** Authentication Keys *********
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

###********** Authentication **********
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

###********** Build a streamListener class that will listen to tweets based on an embedded track list **********
class StreamListener(tweepy.StreamListener):
    #The first method is the constructor, which takes the API for Authentication
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        #Ignores the tweet, so long as I am the Author, or it's a reply to a tweet
        if status.in_reply_to_status_id is not None or \
            status.user.id == self.me.id:
            return

        if hasattr(status, 'retweeted_status'):
            print('{} is not the original author of the tweet. Escaping retweet action....'. format(status.user.screen_name))
            time.sleep(1)
            return
        # if not status.retweeted and not status.is_quote_status:
        #     if status.user.statuses_count < 100:
        #         print('The user has {} number of tweets only'. format(str(status.user.statuses_count)))
        #         # time.sleep(0)
        #         return

        if not status.is_quote_status:
            blocked_users = ['sheikhO12784972','yxvngdvke','cholphela','Gatyangkai20','yahyaah74050732','Salifu14905216','Mutrovic_junior','InsightJuba','EmmsEmms1','permworldcup','happyhealth','blackgayvideo','KenyiKennedy5','BrosMam97','brintonmarcus','KelDuol',
            'HotXXX88086094', 'mehedimxbd','UgandaIllumin13','kakwaSon','AmosAngong','KakuwaSon','BustaLime91','LuxonSpencer','King_Chris_Jr',
            '80daysbot','WarsGenerator','authenticfabric','dengtielakol', 'githeko','AtWarBot','ConstrainBot',
            'whereistheiss','animal_tech_cop', 'MalongThiel','michael27297382','anaabot','GebregziabherW1','Lokudubenjamin1',
            'AC_5230','Thurjang6','michael92367701', 'lyndasc25576386','xpstudiospnguin', 'BrosMam97','richmulondo',
            'SUDANISPICE','MajokBeny','AC_5230','indyfroggy','bot_hamster','Majhi_Marathi','kiha72yufumori','LongLiveLeech',
            'realdavidtarus', 'lilyesha_lilye','RandolphNews1','NILEVONNILE', 'dreadlocks254','DgohnieO','Supp0rtSqu1rrel',
            'ImmigrantsBlack','kirwa400','thirdbrainfx','BlaqGold211','abdullah_who1','QualitySsd','VonBabyJB','VonbabyJB064',
            'MckaylaMyers123','VetsFlagatGmail','gum_ater','EricaGalvin3','_GenocideDenier','Dylan40405249','I_Find_Species','santo_oketayot',
            'The_1_one','Raipperi','jal_biel','every98seconds_','BongaPoppy','edward_apet','ExcusesBot','NyanwangkeiM',
            'undoh','AlexMauricioZe2','manufacturer888','mimi12_sadia',
            'PGHBot','AlemTiop','MahouRoboujo','JustineDhieu','Gatluakofficial','Odumodulfa','enger_mayar',
            'Tajcorp211','samson_FG','kennkiritu']
            user_tweet = status.user.screen_name

            blocked_uza = []
            for uza in blocked_users:
                if uza == user_tweet:
                    blocked_uza.append(uza)
            if len(blocked_uza) != 0:
                print(blocked_uza)
                print('*****************************************************************************************')
                print('*****************************************ADMIN******************************************')
                print('*****************************ALERT! Prohibited from retweets*****************************')
                print('********************Detected that a tweet does not met some criteria!********************')
                print('************************The account owner has been black-listed*************************')
                print('*********Certain accounts specialize in content that might be abusive or erotic**********')
                print('****In cases as such, automatic retweeting is disalbed, even with hashtags like #SSOT****')
                print('*******************************Sorry for any inconveniences******************************')
                print('******************************************ADMIN Manzu Gerald Simon KENYI******************************************')
                print('****************************************************************************************')
                print('The text from the tweet is printed below: - Kindly cross-check.')
                print(status.text)
                print('....................................')
                return
            blocked_words=['dinka','nuer','ethnocide','cheater','Tigray', 'TPLF','genocide','sex','porn','fuck','dog', 'oromo','bokoharam',
            'ugly','horny', 'bitch','penis','vagina','Illuminati', 'pornography','tribes', 'sarmuta',
            'biafra','WarsGenerator','authenticfabric', 'timor','ambazon','Email List',
            'nuer tribe', 'dinka tribe', 'killing','genocide', 'Turkey', 'Russia', 'China', 'India', 'Ethiopia','DECLARED WAR']
            blocked_words_final = []
            for n in blocked_words:
                blocked_words_final.append(n.lower())
            for n in blocked_words:
                blocked_words_final.append(n.upper())
            for n in blocked_words:
                blocked_words_final.append(n.capitalize())

            blocked_words_monitor = []
            for word in blocked_words_final:
                if word in status.text:
                    blocked_words_monitor.append(word)
            if len(blocked_words_monitor) != 0:
                print("The blocked words are {} and nothing will be retweeted.".format(blocked_words_monitor))
                print("The text from the tweet is here .......--------...........{}".format(status.text))
                return
            else:
                try:
                    status.retweet()
                    print('+++++++++++++++++++++++++')
                    print("Retweeted tweet from "+ status.user.screen_name)
                    print('+++++++++++++++++++++++++')
                    print(status.text)
                    print('+++++++++++++++++++++++++')
                    time.sleep(25)
                    return
                except tweepy.error.TweepError as e:
                    print("Error on_data %s" % str(e))
                    return e
    def on_error(self, status_code):
        if tweepy.error.TweepError:
            print("Error from limits")
            raise tweepy.error.TweepError
#Calling the class
stream_listener = StreamListener(api)
#Connecting the listener to the Stream
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#Passing a items into a list that will be used as a track list. The bot retweets anything that mentions the following
ssd_list = ["South Sudan","South Sudanese","#SouthSudanese","junubin","junub bot","junubeen","#SSOT_tweets","#SouthSudan","#SSOT", "@junub_bot","gerald manzu"]
#The dot filter method takes one parameter, the list to be tracked.
lang_retweets = ['en-GB', 'en-IE', 'en-US', 'en-ZA', 'ar-SA']
stream.filter(track= ssd_list)
###********** END **********
###********** END **********
###********** END **********
