from twython import Twython, TwythonError

TWITTER_APP_KEY = '5MzWvWdFZyE4W929IB7bIsaEB'
TWITTER_APP_KEY_SECRET = 'RC7uZ2MYzwKlOkHJjiFSfJh2G7orIqzhZu5U80mb7Gugbl2uPj'
TWITTER_ACCESS_TOKEN = '248913490-3ZbvWRcb3XANELXflUs8oZCdHi0IXAC48Zq3GB4s'
TWITTER_ACCESS_TOKEN_SECRET = 'tjBQrFpUrxMvVWiIz4hZGwxmvGR14tHzG2USFugvZ8exd'

t = Twython(app_key = TWITTER_APP_KEY, app_secret = TWITTER_APP_KEY_SECRET, oauth_token = TWITTER_ACCESS_TOKEN, oauth_token_secret = TWITTER_ACCESS_TOKEN_SECRET)

# Input query and number of tweets to favorite

def fav(qry,ct=1):

    search = t.search(q=qry, count=ct)
    tweets = search['statuses']
    numfav = 0
    
    for tweet in tweets:
        try:
            t.create_favorite(id=tweet['id'])
            numfav += 1 
            print 'Favorited',numfav,'tweets: '+tweet['text'][0:50]
        except TwythonError as e:
            print e
    print "Successfully favorited",numfav,'out of',ct,'tweets!'
        
# Request raw inputs and run fav

term = '#'+raw_input('Term to favorite? ')
numfav = int(raw_input('Number of favorites? '))

fav(term,numfav)
