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


@bot.command()        
async def ping(ctx):
    await ctx.send('hello!')


@bot.command()
async def hi(ctx,name):
    await ctx.send(f"Hello, `{name}`.")

    
@bot.command()
async def time(ctx):
    await ctx.send(datetime.datetime.now(tokyo_tz))
    
    
bot.run(token)                  
