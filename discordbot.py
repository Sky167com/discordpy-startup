from discord.ext import commands
import os
import traceback
import datetime


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

@bot.command()        
async def ping(ctx):
    await ctx.send('hello!')


@bot.command()
async def 何時(ctx):
    await ctx.send(datetime.datetime.now)


@bot.command()
async def hi(ctx):
    await ctx.send('こんにちは')

#一部隠す。    
@bot.command()
async def 時間(ctx):
    await ctx.send('今は'+str(datetime.datetime.now(tokyo_tz))+'です。')
#ヒントを作る    
@bot.command()
# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信



bot.run(token)                  
