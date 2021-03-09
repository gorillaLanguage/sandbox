# インストールした discord.py を読み込む
import discord
import sys

# 自分のBotのアクセストークンに置き換えてください
TOKEN = sys.argv[1]

# チャンネルのID
CHANNELID = 767327887719399446

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('login')
    await oha()

async def oha():
    channel = client.get_channel(CHANNELID)
    await channel.send('ﾏｲﾝｸﾗﾌﾄｻｰﾊﾞｰ 管理ﾎﾞｯﾄ ﾀﾞﾖ')
    await channel.send('ﾎﾞｸｶﾞｵﾝﾗｲﾝﾉ時 ﾊ ｻｰﾊﾞｰ起動中 ﾀﾞﾖ')
    await channel.send('ｿﾉｳﾁ 色々ﾃﾞｷﾙﾖｳﾆﾅﾙ ｹﾄﾞ 今ﾊｳﾝｺﾎﾞｯﾄ ﾀﾞﾖ')


#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    
    #キーワードリスト
    messageList = {
        'neko':'ﾆｬｰﾝ'
        ,'うんこ':'ｳﾝｺｫｫｫｫｫｫｫｫｫ!!!!!'
        ,'うんこよし！':'ｳﾝｺﾖｼ!'
        }

    #ライブラリからキーワード持ってきて返す
    if message.content in messageList:
        await message.channel.send(messageList[message.content])

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)