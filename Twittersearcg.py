import tweepy

auth = tweepy.OAuthHandler('gdT9Z3Pt22LAaM6EBJ6ZsPmXw','aSlc67r2NCSG4gjhTa8IbY4O4fQ5XXCfTZsFaCJubfqLkdPS07')
auth.set_access_token('24850991-qmvMhxBqSGMGGqvAlzIV4osP85rfO22l949b2NbtZ','f4JHDn2GjB7Ez5QMOyDAmTjMPoV2h7IOsQeTJpIQnzP52')

twitter_api = tweepy.API(auth)

city =(str(raw_input ('Which city would you like to explore? (City, Country) \n'))).split()

search_place= city [0]

london_tweets = twitter_api.search(
    q="{search_place}",
    result_type="recent"

)

for tweet in london_tweets:
        print tweet.text