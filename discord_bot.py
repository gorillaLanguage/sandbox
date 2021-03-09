# インストールした discord.py を読み込む
import discord
import sys

# 自分のBotのアクセストークンに置き換えてください
TOKEN = sys.argv[1]

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    
    messageList = {
        'neko':'ﾆｬｰﾝ'
        ,'うんこ':'ｳﾝｺｫｫｫｫｫｫｫｫｫ!!!!!'
        ,'うんこよし！':'ｳﾝｺﾖｼ!'
        }

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content in messageList:
        await message.channel.send(messageList[message.content])


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)