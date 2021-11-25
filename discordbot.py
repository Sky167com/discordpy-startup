from discord.ext import commands
import os
import traceback
import datetime
import schedule



bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_ready():
    await print('ログインしました。')

from time import sleep

@bot.event
async def task():
    await ctx.send("HELOO")
schedule.every().days.at("12:30").do(task)
    while True:
        schedule.run_pending()
        sleep(1)
    
@bot.command()        
async def ping(ctx):
    await ctx.send('hello!')


@bot.command()
async def 何時(ctx):
    await ctx.send(str(datetime.datetime.now))


@bot.command()
async def hi(ctx):
    await ctx.send('こんにちは')

#一部隠す。    
@bot.command()
async def time(ctx):
    await ctx.send('今は'+(str(datetime.datetime.now(tokyo_tz))[:19])+'です。')
#ヒントを作る    


bot.run(token)                  
