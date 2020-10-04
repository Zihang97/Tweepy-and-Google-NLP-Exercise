# Tweepy
Explore the tweepy function
## Grad the recent 20 tweets of specific user
```
public_tweets = api.user_timeline(username)
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))
```

<p align="left">
    <img src="https://github.com/Zihang97/Tweepy-and-Google-NLP-Exercise/blob/master/Picture/user_timeline.PNG" width="600"/>
</p>

My print has some \x symbols as I ran it on windows, which is hard to deal with some utf codes.

## Search tweets
```
alltweets=tweepy.Cursor(api.search,q='Tenet').items(1)
for tweet in alltweets:
	print(tweet.text.encode('utf-8'))
```
<p align="left">
    <img src="https://github.com/Zihang97/Tweepy-and-Google-NLP-Exercise/blob/master/Picture/search.PNG" width="600"/>
</p>

# Google-NLP
Test on different Google NLP APIs and mainly focus on sentiment analysis

## Command Line Exercise
Following the steps in natural language API quickstarts
1. Create a project called Project2-Sentiment Analysis on cloud console
2. Enable billing and cloud natural language API
3. Create a service account and download private key file used in my environment (each new terminal has to reset the credentials again)
4. Install and initialize cloud SDK 
5. Try the command line

### Entity

```
gcloud ml language analyze-entities --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'."
```

Succeed!

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/image.png" width="600"/>
</p>

### Sentiment

```
gcloud ml language analyze-sentiment --content="I love puppies."
```

Succeed! (I found that I have to use double quotes here, using single quotes leading to one word read)

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/Sentiment.PNG" width="200"/>
</p>

## Client Library Exercise
I spent a lot of time on this part as at the beginning I found my python script fell into infinite loop.
After searching I found I was blocked by the firewall as I can't make a post request to https://language.googleapis.com

```
curl language.googleapis.com
```

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/Curl_failed.PNG" width="600"/>
</p>

But after I set up the proxy in environment, I get access to google language server successfully.

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/curl_succeed.PNG" width="600"/>
</p>

Then I ran my python script [Hello world](https://github.com/Zihang97/Google-NLP/tree/master/Code/sentiment_no_function.py) which succeeded.

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/hello_world.PNG" width="400"/>
</p>

The result of script [happy and joyful](https://github.com/Zihang97/Google-NLP/blob/master/Code/language_sentiment_text.py)

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/happy and joyful.PNG" width="400"/>
</p>

The result of script [sad](https://github.com/Zihang97/Google-NLP/blob/master/Code/sentiment_analysis.py)

<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/sad.PNG" width="400"/>
</p>


