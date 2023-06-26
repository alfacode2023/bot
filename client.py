import random as r
import asyncio
from asyncio import *
import sys
import time as tm
from colorama import init
init()
from colorama import Fore


import discord
from discord.ext import commands as com


TOKEN = 'MTExODE1NjgxNzk0NDU0MzI4NQ.G47vTy.Z92WrdBRibRvketmnTeNeRZqJoKuTx9OXJEYO4'

client = com.Bot(command_prefix= '//', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print(Fore.YELLOW+f'We have logged in as {client.user}')
    act = discord.Game(name= '//help', type = 2)
    await client.change_presence(status=discord.Status.idle, activity=act)

@client.command()
async def spam(ctx,count):
    for i in range(int(count)):
        s = ""
        for i in range(2000):
            s += str(chr(r.randint(97, 122)))
        await ctx.send((s + "\n") * 1)

@client.command()
async def clear(ctx: discord.ext.commands.Context, count):
    if count == "all":
        q = await ctx.channel.purge()
        await ctx.send(embed = discord.Embed(description='همه ی پیام ها حذف شدند', colour=0x374642))
    else: 
        count = int(count)
        count += 1
        await ctx.channel.purge(limit= count)
        if count > 2:
            await ctx.send(embed = discord.Embed(description=str(count - 1) + 'پیام حذف شدند', colour=0x283654))
        else:
            await ctx.send(embed = discord.Embed(description='یک پیام حذف شد', colour=0x275642))

@client.command()
async def post(ctx, title = 'test', thumb = None, image = None,*, text = 'the example text'):
    cs = [0xff0000, 0x66ff66,0x0000ff]
    cs = r.choice(cs)
    membed = discord.Embed(
        title='>>> '+title,
        description=text,
        colour= cs
    )
    if thumb != 'no':
        membed.set_thumbnail(url= thumb)
    if image != 'no':
       membed.set_image(url= image)
    await ctx.channel.purge(limit= 1)
    await ctx.send(embed= membed)

@client.command()
async def code(ctx, lang = 'python3.11', *, code):
    mt = lang
    membed = discord.Embed(
        title= mt,
        description='```'+ code + '```',
        colour=0x0000ff
    )
    n = ctx.author.mention
    membed.set_footer(text=n,icon_url='https://s27.picofile.com/file/8459782442/m.png')
    await ctx.channel.purge(limit= 1)
    await ctx.send(embed= membed)

@client.command()
async def support(ctx, *, message):
    cembed = discord.Embed(
        description='با موفقیت ارسال شد',
        colour=0x758834
    )
    uembed = discord.Embed(
        description=message,
        colour=0x375345
    )
    n = ctx.author.mention
    user = client.get_user(952960349152366663)
    user1 = client.get_user(818719435673042964)
    await user.send(embed = uembed)
    await user1.send(embed=message)
    await user.send('**'+ "توسط:" + "**"+ n)
    await user1.send('**'+ "توسط:" + "**"+ n)
    await ctx.send(embed = cembed)

@client.command()
async def javab(ctx, cont, *, message):
    uembed = discord.Embed(
        title='پیام از طرف پشتیبانی',
        description=message,
        colour= 0xff0000
    )
    membed =discord.Embed(
        title=':)',
        description='با موفقیت ارسال شد',
        colour= 0x0000ff
    )
    asgari = client.get_user(934067159091535922)
    ali = client.get_user(932571324075880499)
    hamid = client.get_user(798156257537949717)
    sar = client.get_user(1061273622632726538)
    acc2 = client.get_user(1088842320608243762)
    if cont == 'acc2':
        await acc2.send(embed= uembed)
        await ctx.send(embed = membed)
    elif cont == 'asgari':
        await asgari.send(embed= uembed)
        await ctx.send(embed = membed)
    if cont == 'ali':
        await ali.send(embed=uembed)
        await ctx.send(embed=membed)
    elif cont == 'hamid':
        await hamid.send(embed=uembed)
        await ctx.send(embed=membed)
    elif cont == 'sar':
        await sar.send(embed=uembed)
        await ctx.send(embed=membed)
    else:
        contact = client.get_user(int(cont))
        await contact.send(embed=uembed)
        await ctx.send(embed=membed)

@client.command()
async def help(ctx):
    membed = discord.Embed(
        title='>>> لیست کامند ها',
        description="**//clear** \n جلوش تعداد پیام هایی رو که میخواین مینویسین اونم پاک میکنه\n فقط باید دقت کنید که تو چنر عمومی باشه\n -------------------- \n **//code** \n اینم باید توچنل عمومی استفاده کنید \n باید کامند رو بنویسید بعد زبان کد و بعد  کد رو پیست کنید\n--------------------\n**//support**\n اگر کاری با پشتیبان داشتید این کامند رو بنویسید و بعد پیامتون روبنویسید ",
        colour=  0x66ff66,
    )
    membed.set_footer(text='code assistantbot', icon_url='https://s27.picofile.com/file/8459782442/m.png')
    membed.set_author(name='help')
    await ctx.send(embed= membed)

@client.command()
async def stop(ctx):
    admin = ctx.author.mention
    if admin == '<@952960349152366663>':
        await ctx.send(embed = discord.Embed(title= "هویت ادمین تایید شد", description='ربات در 10 ثانیه دیگر خاموش میشود', colour= 0x534786))
        act = discord.Game(name= 'turned off', type = 3)
        await client.change_presence(status=discord.Status.invisible, activity=act)
        tm.sleep(10)
        sys.exit()
    else:
        await ctx.reply('هویت شما برای خاموش کردن ربات تایید نشد')

@client.command()
async def main(ctx, *,mes):
    chan = client.get_channel(1101905616638849104)
    await chan.send(mes)


client.run(TOKEN)