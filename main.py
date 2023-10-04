import os
import requests
import time
import json
import fgourl
import user
import coloredlogs
import logging

# Enviroments Variables
userIds = os.environ['userIds'].split(',')
authKeys = os.environ['authKeys'].split(',')
secretKeys = os.environ['secretKeys'].split(',')
fate_region = os.environ['fateRegion']
webhook_discord_url = os.environ['webhookDiscord']
UA = os.environ['UserAgent']

if UA != 'nullvalue':
    fgourl.user_agent_ = UA

userNums = len(userIds)
authKeyNums = len(authKeys)
secretKeyNums = len(secretKeys)

logger = logging.getLogger("FGO Daily Login")
coloredlogs.install(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


def get_latest_verCode():
    endpoint = ""

    if fate_region == "NA":
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/NA/VerCode.json"
    else:
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/JP/VerCode.json"

    response = requests.get(endpoint).text
    response_data = json.loads(response)

    return response_data['verCode']


def main():
    if userNums == authKeyNums and userNums == secretKeyNums:
        logger.info('Getting Lastest Assets Info')
        fgourl.set_latest_assets()

        for i in range(userNums):
            try:
                instance = user.user(userIds[i], authKeys[i], secretKeys[i])
                time.sleep(3) # 开始抽卡前的账号信息
                logger.info('Loggin into account!')
                instance.topLogin()
                time.sleep(2)
                instance.topHome()
                time.sleep(2)
                logger.info('Throw daily friend summon!')
                
                try:
                   instance.drawFP() 
                   time.sleep(2)
                   for _ in range(500): # 输入你要抽几次10连（默认501次） 举个栗子： 100=101 / 1=2 / 99=100 / 999=1000
                      instance.drawFP()
                      time.sleep(0.1)  # 抽卡速度过快，禁用了DC抽卡结果发送消息功能，所以自己查看结束后的友情点数
                except Exception as ex:
                    logger.error(ex)
                    
                try:
                   time.sleep(3)  # 结束后的账号信息
                   logger.info('Loggin into account!')
                   instance.topLogin()
                   time.sleep(2)
                except Exception as ex:
                    logger.error(ex)
            
            except Exception as ex:
                logger.error(ex)


if __name__ == "__main__":
    main()
