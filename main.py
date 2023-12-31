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
blue_apple_cron = os.environ.get("MAKE_BLUE_APPLE")


UA = os.environ['UserAgent']

if UA:
    fgourl.user_agent_ = UA

userNums = len(userIds)
authKeyNums = len(authKeys)
secretKeyNums = len(secretKeys)

logger = logging.getLogger("FGO 自动抽卡系统")
coloredlogs.install(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


def check_blue_apple_cron(instance):
    if blue_apple_cron:

        cron = croniter(blue_apple_cron)
        next_date = cron.get_next(datetime)
        current_date = datetime.now()
        
        if current_date >= next_date:
            logger.info('Trying buy one blue apple!')
            instance.buyBlueApple(1)
            time.sleep(2)


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
                time.sleep(2) # 开始抽卡前的账号信息
                logger.info('登录账号!')
                instance.topLogin()
                time.sleep(2)
                instance.topHome()
                time.sleep(2)
                    
                try:
                   logger.info('开始友情点召唤!')
                   instance.drawFP() 
                   time.sleep(2)
                   for _ in range(500): # 输入你要抽几次10连（默认501次） 举个栗子： 100=101 / 1=2 / 99=100 / 999=1000 / 500=501
                      instance.drawFP()
                      time.sleep(0.1)  # 抽卡速度过快，禁用了DC抽卡结果发送消息功能，所以自己查看结束后的友情点数
                except Exception as ex:
                    logger.error(ex)
            
            except Exception as ex:
                logger.error(ex)


if __name__ == "__main__":
    main()
