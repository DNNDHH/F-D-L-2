<img width="100%" style="border: 1px solid black" src="https://i.imgur.com/bre34Xl.png">

<img width="100%" style="border: 1px solid black" src="https://i.imgur.com/YHWRq2l.png">

# FGO自动登录系统（Python发包程序）（中文版）
😒封号风险自行承担👌

🫠注意，为保证定时登录生效，你需要每60天更新一次这个库，这是github自动流程的要求🫠

✅作者 [O-Isaac] https://github.com/O-Isaac/FGO-Daily-Login

FGO自动登录是基于此项目的MOD [FGODailyBonus](https://github.com/hexstr/FGODailyBonus)

它具有以下特点：
- 无日志
- 全自动游戏版本更新
- 向你的Discord频道发送登录结果
- 只支持 JP 和 NA 版本

# 提取您的 游戏身份验证数据
您需要提取身份验证数据才能执行此操作。
很简单，您所需要做的就是导航到以下路径并获取以下文件： 

| 版本 | 文件路径 | 文件名称 |
| --- | --- | --- | 
| NA | `android/data/com.aniplex.fategrandorder.en/files/data/` | 54cc790bf952ea710ed7e8be08049531 |
| JP | `android/data/com.aniplex.fategrandorder/files/data/` | 54cc790bf952ea710ed7e8be08049531 |

# 解密您的游戏账号数据
请小心处理这些数据，您不应将此数据传递给其他人，这是直接与服务器通信的私人数据。

1. 用记事本或文本编辑器打开文件并从**ZSv**复制到结束！
2. 转到 [在线解析](https://dotnetfiddle.net/ug7C0x) 并粘贴字符串
3. 您将获得填写 密钥 所需的所有数据
4. 获取您设备（手机或模拟器）的用户代理 [从这里](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)

# 创建 Discord 消息通知机器人
要创建 webhook Discord，您需要在 Discord 中创建一个服务器 并在该频道的 设置中 创建一个 文本频道
`integration > webhook > create webhook > copy url webhook`

# 执行定时签到任务/定时登录
我配置这个存储库的 cron [游戏版本代码 VerCode 提取器存储库](https://github.com/O-Isaac/FGO-VerCode-extractor)
您应该在更新 游戏版本代码 VerCode 提取器存储库 后配置所有 cron！

| 版本 | 游戏版本代码 提取器存储库     | 定时登录FGO的时间（世界时UTC+00）      |
|--------|-------------|-------------|
| NA     | 15 10 * * * | 30 10 * * * |
| JP     | 15 19 * * * | 30 19 * * * |

🫠我已经修改为 天朝时间 中午 12：00 登录第一次 12：30登录第二次！

没有必要再次更改其它的游戏版本 verCode 仓库，但如果你想这么干的话
则必须更改函数中 main.py 中的该值 `get_latest_verCode`

# 填写 游戏账号密钥
将此下列类型添加到 `右上角 > settings > Secrets and variables > actions`
| 密钥 | 样本 |
| --- | --- |
| GAME_AUTHKEYS | RaNdOmStRiNg1234:randomAAAAA=,RaNdOmStRiNg1235:randomAAAAA= |
| GAME_SECRETKEYS | RaNdOmStRiNg1234:randomAAAAA=,RaNdOmStRiNg1235:randomAAAAA= |
| GAME_USERAGENT | Dalvik/2.1.0 (Linux; U; Android 11; Pixel 5 Build/RD1A.201105.003.A1) or Your User Agent |
| GAME_USERIDS | 60951234,60951235 |
| GAME_REGION | NA or JP (Must be in upper case) |
| DISCORD_WEBHOOK | https://discord.com/api/webhooks/randomNumber/randomString |

# 未来计划 （咕咕咕🤣）
- [x] 自动每日友情点召唤
- [ ] 自动领取礼物盒自动兑换材料票
- [ ] 自动种蓝苹果🍎

# 特别鸣谢
- [hexstr](https://github.com/hexstr) FGO自动登录系统 作者
