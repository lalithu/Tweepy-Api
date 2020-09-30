import tweepy
import time

authid = "BR1dPIeKC3ORjda7a4YKqH4xj"
authkey = "kFs6kZ9ZhtCKzrVnb4Ggpz2LwwmUaxT3xlykE0XRgEybWqjEU3"

tokenid = "1294345533050351616-35hpysbpO3XGANp0Nviwnssjh9IXDr"
tokenkey = "yl6tF9C5CH27rKzSkOqca0DasQxGoySdyOnpc7HCPePlF"

auth = tweepy.OAuthHandler(authid, authkey)
auth.set_access_token(tokenid, tokenkey)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Unsuccessful")

user = api.me()

print("Follower Count: ", user.followers_count)

search = 'Java'
nrTweets = 500
likeCounter = 0
retweetCounter = 0

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        likeCounter += 1
        print("Tweet Liked | ", likeCounter)
        tweet.favorite()
        time.sleep(20)

        retweetCounter += 1
        print("Tweet Retweeted | ", retweetCounter)
        tweet.retweet()
        time.sleep(20)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
