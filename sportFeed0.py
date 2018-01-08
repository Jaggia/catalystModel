from ohmysportsfeedspy import MySportsFeeds
from pymongo import MongoClient
from bson import json_util

msf = MySportsFeeds(version="1.0")
msf.authenticate("Jaggia", "pxt-7xc-PtG-sSk")

response = msf.msf_get_data(league='nba',
                            season='2016-2017-regular',
                            feed='cumulative_player_stats',
                            format='json',
                            team='chi')


client = MongoClient()
db = client.sportsDB
posts = db.posts
post_id = posts.insert_one(response).inserted_id
print post_id


# print(response)
