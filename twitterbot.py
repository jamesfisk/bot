from markovdict import *
from local_settings import *
import io
import twitter
import random


def connectAPI():
  api = twitter.Api (consumer_key=MY_CONSUMER_KEY, consumer_secret=MY_CONSUMER_SECRET, access_token_key=MY_ACCESS_TOKEN_KEY, access_token_secret=MY_ACCESS_TOKEN_SECRET)
  return api

def main():
  strlist = io.open("plath.txt", "r", encoding='utf-8').read().split()
  model = markovdict(strlist)
  api = connectAPI()

  tweet = model.get_sentence()

  while (len(tweet) > 140):
    tweet = tweet.rsplit(' ', 1)[0]
  will_post = random.random()
  if (will_post > .4):
    api.PostUpdate(tweet)

main()
