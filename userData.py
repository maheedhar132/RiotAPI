import  requests
import os
headers = {
    'Content-Type': 'application/json',
    'X-Riot-Token': os.getenv('riot_token')
    }

def getPlayerData(summonerName,region):
    url = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName
    response = requests.request("GET",url,headers=headers)
    return response.text

def getSummonerRank(encryptedID,region):
    url = "https://"+region+".api.riotgames.com/tft/league/v1/entries/by-summoner/"+encryptedID
    response = requests.request("GET",url,headers=headers)
    return response.text
