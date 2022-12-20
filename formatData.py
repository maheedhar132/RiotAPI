import json
def getEncryptedId(data):
    result=json.loads(data)
    return result['id']

def getAccountId(data):
    result=json.loads(data)
    return result['accountId']

def getPuuid(data):
    result=json.loads(data)
    return result['puuid']

def getPlayerRank(data):
    result = json.loads(data)
    hyper_roll_rank = result[0]['ratedTier']
    hyper_roll_rating = str(result[0]['ratedRating'])
    hyper_roll_total = "Hyper ROLL: "+hyper_roll_rank+" "+hyper_roll_rating
    ranked_tier = result[1]['tier']
    ranked_rank = result[1]['rank']
    ranked_leaguePoints = str(result[1]['leaguePoints'])
    ranked_total = "Ranked: "+ranked_tier+" "+ranked_rank+" "+ranked_leaguePoints
    total_output = hyper_roll_total+"\n"+ranked_total
    return total_output

