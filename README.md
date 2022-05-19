# JunuBot
### A Twitter Retweet Bot
![image](https://user-images.githubusercontent.com/23518337/123507632-72dd8480-d6a5-11eb-88ac-8d8d1ed7a477.png)


This project is specifically built to actively listen to tweets, like and retweet them for a research module...
It uses open source tools to interract with twitter, and host/ launch online. These include:
1. Built using Python
2. Uses the Tweepy Library, for Accessing the Twitter API
3. Hosted on GitHub (Any changes updated in the main branch automatically launches on Heroku, where the app is hosted)
4. Uses Heroku for hosting / running the bot 24/7 with a heroku account

### More about the Bot
Junub Bot streams Twitter and actively listens to tweets that contain elements passed in a list. Any Tweet mentioning words in the list are automatically favourited (liked), and then retweeted.

![image](https://user-images.githubusercontent.com/23518337/123507537-ea5ee400-d6a4-11eb-91b8-07c49cda4831.png)

###Feel free to use this code!

###MORE ON HOSTING THE BOT ON HEROKU
First things first
<ul>
  I'm assuming you've got a Twitter Developer account and can generate the Authentication keys for your APP.
  Otherwise apart from the python code for the bot, Heroku needs to know about two files. The Procfile and the requirements.txt file. The Procfile shouldn't have any extension and should be in the root directory. The requirements file often tells Heroku what to install so as to run your app. To generate this file, run 'pip freeze> requirements.txt' without the quotes. These are the two necessary files, plus your python file that will enable Heroku to host the bot.
  </ul>

1. Create a Heroku account
2. Then create a Heroku App

![image](https://user-images.githubusercontent.com/23518337/123507772-5130cd00-d6a6-11eb-8db6-41182c88a770.png)

3. In the DEPLOY tab, you can choose between using Heroku CLI or Github. For this project, I deployed it via Github
4. Make sure to enable automatic deploys so that any changes made on Github are reflected on Heroku, immediately.

![image](https://user-images.githubusercontent.com/23518337/123507856-e5029900-d6a6-11eb-9908-8c9ce1f96621.png)

5. Turn on the APP from the Overview Tab, Dyno information

![image](https://user-images.githubusercontent.com/23518337/123507879-1bd8af00-d6a7-11eb-9840-f79dabe51bab.png)

6. In the settings TAB, add the Tweepy API KEYS - To do this, click on Config Vars. Make sure that the same name they were called in the python file are exactly the same here.

#The code in the python file has the following variable names.... they should be the same in Heroku

![image](https://user-images.githubusercontent.com/23518337/123507967-a0c3c880-d6a7-11eb-8a15-90833ce3d2b0.png)


##Config Vars in Heroku
![image](https://user-images.githubusercontent.com/23518337/123507935-7114c080-d6a7-11eb-962d-bb84e2fe858f.png)

7. Finally, check whether Heroku is up and running....
Go to Settings and click on More.....

![image](https://user-images.githubusercontent.com/23518337/123508006-d23c9400-d6a7-11eb-9ce9-cebe530d18e7.png)

Then click on View Logs

![image](https://user-images.githubusercontent.com/23518337/123508042-fac48e00-d6a7-11eb-9e31-67880ec79ec4.png)


###Yeah! That's it! Your bot should be up and running....

###Will include a link to a demo video soon! Cheers
