from TwitterAPI import TwitterAPI

from pprint import pprint

from keys import *

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'pizza'})


if (r.status_code==200):
  for item in r.get_iterator():
    pprint(item)

    
