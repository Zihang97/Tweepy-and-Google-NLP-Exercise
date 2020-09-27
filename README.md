# Google-NLP
Test on different Google NLP APIs and mainly focus on sentiment analysis

## Command Line try
Following the steps in natural language API quickstarts
1. Create a project called Project2-Sentiment Analysis on cloud console
2. Enable billing and cloud natural language API
3. Create a service account and download private key file used in my environment (each new terminal has to reset the credentials again)
4. Install and initialize cloud SDK 
5. Try the command line
```
gcloud ml language analyze-entities --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'."
```
Succeed!
![Image](https://github.com/Zihang97/Google-NLP/blob/master/Picture/image.png)
