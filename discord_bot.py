import discord
import sys
import subprocess as sub

TOKEN = sys.argv[1] #トークン
CHANNELID = 767327887719399446 #チャンネルID
client = discord.Client() #ディスコードインスタンス生成

#キーワードリスト
messageList = {
    'test':'test message'
    ,'うんこ':'ｳﾝｺｫｫｫｫｫｫｫｫｫ!!!!!'
    ,'うんこよし！':'ｳﾝｺﾖｼ!'
    }



@client.event
async def on_ready(): #起動時に動作する処理
    print('login')
    await minecraftServerStart()
    #await oha() #起動時に挨拶　うるせーからいったんコメントアウト

async def oha(): #挨拶
    channel = client.get_channel(CHANNELID)
    await channel.send('ﾏｲﾝｸﾗﾌﾄｻｰﾊﾞｰ 管理ﾎﾞｯﾄ ﾀﾞﾖ')
    await channel.send('ﾎﾞｸｶﾞｵﾝﾗｲﾝﾉ時 ﾊ ｻｰﾊﾞｰ起動中 ﾀﾞﾖ')
    await channel.send('ｿﾉｳﾁ 色々ﾃﾞｷﾙﾖｳﾆﾅﾙ ｹﾄﾞ 今ﾊｳﾝｺﾎﾞｯﾄ ﾀﾞﾖ')



@client.event
async def on_message(message): #メッセージ受信時に動作する処理
    await reply(message)
    await reaction(message)

async def reply(message): #リプライ
    if client.user in message.mentions:
        message.channel.send('ﾅﾝﾔﾎﾞｹｪ!')


async def reaction(message): #通常メッセージ
    #ライブラリからキーワード持ってきて返す
    if message.content in messageList:
        await message.channel.send(messageList[message.content])

async def minecraftServerStart():
    sub.call(['/home/pi/Desktop/program/server/start.sh'])


client.run(TOKEN) #Botの起動とDiscordサーバーへの接続