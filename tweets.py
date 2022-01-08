import tweepy as tw # This is a package for accessing the Twitter API

import pandas as pd # This a python library for manipulating data

import json # Allows us to work with JSON files

if __name__ == '__main__':
    
    # Extract our API keys from the JSON file
    with open("twitter_cred.json", "r") as f:
        creds = json.load(f)
        
    consumer_key = creds["CONSUMER_KEY"]
    consumer_secret = creds['CONSUMER_SECRET']
    access_token = creds['ACCESS_TOKEN']
    access_secret = creds['ACCESS_SECRET']
    
    # Run some authentication steps
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tw.API(auth)
    
    for tweet in tw.Cursor(api.search_tweets, q = '#100DaysOfCode', count = 100).items():
        print(tweet)

    