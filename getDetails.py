import userData
import formatData

playerData = userData.getPlayerData('PowJinxed','euw1')

encryptedID = formatData.getEncryptedId(playerData)

playerRankData = userData.getSummonerRank(encryptedID,'euw1')

playerRank = formatData.getPlayerRank(playerRankData)

print(playerRank)