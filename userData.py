import  requests
import os
def getEncrypedID(summonerName,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName
    headers = {
    'Content-Type': 'application/json',
    'X-Riot-Token': os.getenv('riot_token')
    }
    response = requests.request("GET",url,headers=headers)
    return response.text
