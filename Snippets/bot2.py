import asyncio
import discord
import pickle
import random
from discord.ext import commands
description = '''My Personal Bot.'''
auth = '(REDACTED)'
botA = commands.Bot(command_prefix='?', description=description)
auth_users = [641083262856593418]
gore_list = []


def preserve(rawing, storage):
    pickling_on = open(storage + '.pickle', 'wb')
    pickle.dump(rawing, pickling_on)
    pickling_on.close()


def unpreserve(rawing, storage):
    pickle_off = open(storage + '.pickle', "rb")
    rawing = pickle.load(pickle_off)
    print('Unpreserved List:', rawing)
    return rawing


@botA.event
async def on_ready():
    print('[BOT] Created.')


@botA.command()
async def bomb(ctx, channel: int, amount: int, *, args):
    unpreserve()
    if ctx.author.id in auth_users or '641083262856593418':
        channel_bomb = botA.get_channel(channel)
        await ctx.send('Beginning Carpet Bombing')
        for i in range(amount):
            await channel_bomb.send(f'{str(args)} {random.randrange(0, 1000)}')
            await asyncio.sleep(0.25)
    else:
        await ctx.send('Access Denied')


@botA.command()
async def admincheck(ctx):
    unpreserve()
    if ctx.author.id in auth_users or '641083262856593418':
        print('Person Authenticated')
        await ctx.send('Person Authenticated')
    else:
        print('Person Not Reckognized')
        await ctx.send('Person Not Reckognized')


@botA.command()
async def adminauth(ctx):
    unpreserve()
    if ctx.author.id in auth_users or '641083262856593418':
        mention_ids = [mention.id for mention in ctx.message.mentions]
        mention_names = [mention.name for mention in ctx.message.mentions]
        for i in mention_ids:
            auth_users.append(i)
            print(auth_users)
        for i in mention_names:
            print(i, 'has been Authenticated')
            await ctx.send('Persons have been Authenticated')
        preserve(auth_users, 'users')
    else:
        print('Access Denied')
        await ctx.send('Access Denied')


@botA.command()
async def admindeauth(ctx):
    if ctx.author.id == '641083262856593418':
        mention_ids = [mention.id for mention in ctx.message.mentions]
        mention_names = [mention.name for mention in ctx.message.mentions]
        for i in mention_ids:
            auth_users.remove(i)
            print(auth_users)
        for i in mention_names:
            print(i, 'has been Removed')
            await ctx.send('Persons have been Removed')
        preserve(auth_users, 'users')
    else:
        print('Access Denied')
        await ctx.send('Access Denied')


loop = asyncio.get_event_loop()
loop.create_task(botA.start(auth, bot=False))
loop.run_forever()
