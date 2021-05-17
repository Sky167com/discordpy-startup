from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('hello!')


@bot.command()
async def hi(ctx):
    await ctx.send('hi')


date = datetime.datetime.now()
hour = date.hour
min = date.minute

@client.event
async def on_ready():
    print('時報機が起動しました。')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '何時？':
        await message.channel.send(str(hour) + '時です。')
    if message.content == '何分？':
        await message.channel.send(str(min) + '分です。')
    if message.content == '何時何分？':
        await message.channel.send(str(hour) + '時' + str(min) + '分です。')


bot.run(token)                  
