from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import time



start_time = time.time()
UID = "sorry" 
SECRET = "sorry" 


client = BackendApplicationClient(client_id=UID)
api = OAuth2Session(client=client)
token = api.fetch_token(token_url="https://api.intra.42.fr/oauth/token", client_id=UID, client_secret=SECRET, scope="public profile projects")
api.headers.update({"Authorization": "Bearer " + token['access_token']})
a=1
while(a > 0):
    req = api.get("https://api.intra.42.fr", params={"page[size]":100,"page[number]":a})
    list = req.json()
    c=0
    time.sleep(0.6)
    for i in list:
         
    a+=1
