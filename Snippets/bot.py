import discord
import requests
from discord.ext import commands
import asyncio
import random
import pprint
import twint
import json

# Defined Vars
token = '(REDACTED)'
client_id = '647019102266851338'
description = '''A General Infomation Bot'''
Info_Bot = commands.Bot(command_prefix='>', description=description)
permissions = 8


@Info_Bot.event
async def on_ready():
    print('Ready\n' + 'logged in as:')
    print('\t', Info_Bot.user.name + '#' + Info_Bot.user.discriminator)
    print('\t', Info_Bot.user.id)
    print('Total Servers:', len(Info_Bot.guilds))
    print('Login URL:',
          discord.utils.oauth_url(client_id))


@Info_Bot.command()
async def qpicture(ctx, *, args):
    r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 5,
        'q': args,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)
    response = r.json().get('data').get('result').get('items')
    titles = [r.get('title') for r in response]
    urls = [r.get('media') for r in response]
    pprint.pprint(response)
    for i, j in zip(titles, urls):
        i = i.replace('<b>', '**').replace('</b>', '**')
        await ctx.send(i + '\n' + j)
        await asyncio.sleep(0.21)


@Info_Bot.command()
async def qsearch(ctx, *, args):
    r = requests.get("https://api.qwant.com/api/search/web",
    params={
        'count': 5,
        'q': args,
        't': 'web',
        'safesearch': 1,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)
    response = r.json().get('data').get('result').get('items')
    titles = [r.get('title') for r in response]
    descs = [r.get('desc') for r in response]
    urls = [r.get('url') for r in response]
    pprint.pprint(response)
    for i, j, k in zip(titles, descs, urls):
        # await ctx.send(i + '\n' + j + '\n' + k + '\n')
        i = i.replace('<b>', '**').replace('</b>', '**')
        j = j.replace('<b>', '**').replace('</b>', '**')
        embed = discord.Embed(title=i, url=k, description=j, color=0x6db34d)
        await ctx.send(embed=embed)
        await asyncio.sleep(0.21)


@Info_Bot.command()
async def threads(ctx, board: str, page: int):
    r = requests.get("https://a.4cdn.org/" + board + "/threads.json",
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)
    threadlist = r.json()[page - 1]["threads"]
    threads = [r.get('no') for r in threadlist]
    for r in threads:
        await ctx.send('https://boards.4channel.org/' + board + '/thread/' + str(r))
        await asyncio.sleep(0.21)


@Info_Bot.command()
async def discordscrape(ctx):
    tweets = []
    flatlist = []
    for l in open('twint.json', 'r', encoding="utf8"):
        tweets.append(json.loads(l))
    urls = [r.get('urls') for r in tweets]
    for sublist in urls:
        for item in sublist:
            flatlist.append(item)
    matching = [s for s in flatlist if "discord.gg" in s]
    final = list(set(matching))
    for f in final:
        await ctx.send(f)
        await asyncio.sleep(0.21)
    open('twint.json', 'w').close()
    await ctx.send('Scrape Finished')

Info_Bot.run(token, bot=True)
