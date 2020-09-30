import tweepy
import time

auth = tweepy.OAuthHandler('BR1dPIeKC3ORjda7a4YKqH4xj',
                           'kFs6kZ9ZhtCKzrVnb4Ggpz2LwwmUaxT3xlykE0XRgEybWqjEU3')
auth.set_access_token('1294345533050351616-35hpysbpO3XGANp0Nviwnssjh9IXDr',
                      'yl6tF9C5CH27rKzSkOqca0DasQxGoySdyOnpc7HCPePlF')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

'''try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")'''

user = api.me()

print(user.followers_count)

search = 'Javascript'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
