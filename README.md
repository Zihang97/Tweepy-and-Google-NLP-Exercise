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
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/image.png" width="400"/>
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
Then I ran my python script which succeeded.
<p align="left">
    <img src="https://github.com/Zihang97/Google-NLP/blob/master/Picture/hello_world.PNG" width="400"/>
</p>
