import tweepy

# API credentials from TwitterDev
consumer_key = 'iGlv5oyAgv0MsV66km3nXoDa9'
consumer_secret = 'jVy136uKpOZUB2sWskW6VW9KnpgQE9kGLFcn6H77HnR2bbzL0l'
access_token = '1226982099351150604-tyyOSxkkYLC73iEhaLRB49r27YBU0n'
access_token_secret = 'ZqBGSU6EB9MmLS8ZhHXIyZr4E66Jur73PzYET7e0kuhM4'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_tweets = api.user_timeline(screen_name = 'aaron_bwah', count = 10)

print(user_tweets.txt)