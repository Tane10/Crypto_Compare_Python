# this is the dir needed to run python on this mac (look above)
import requests as rq

r =  rq.get("https://www.coinexchange.io/api/v1/getmarkets")

print(r)