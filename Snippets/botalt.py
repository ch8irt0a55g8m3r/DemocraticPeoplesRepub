import datetime
import discord
from discord.ext import commands
import asyncio
from discord.utils import get

# Defined Vars
token = '(REDACTED)'
client_id = '647019102266851338'
description = '''A General Infomation Bot'''
IBot = commands.Bot(command_prefix='>', case_insensitive=True)
permissions = 8


# Events
async def logging(title, desc, ctx):
    logchan = IBot.get_channel(655195773830430776)
    embed = discord.Embed(title=title, description='Logging')
    embed.set_thumbnail(url="https://i.imgur.com/uIXcXbM.png")
    embed.add_field(name=title, value=desc, inline=True)
    embed.add_field(name="Invoker", value=ctx.author, inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    await logchan.send(embed=embed)
    print(f'Acivity:{title} {desc}')


@IBot.event
async def on_ready():
    print('Ready\n' + 'logged in as:')
    print('\t', IBot.user.name + '#' + IBot.user.discriminator)
    print('\t', IBot.user.id)
    print('Total Servers:', len(IBot.guilds))
    print('Login URL:',
          discord.utils.oauth_url(client_id))
    logchan = IBot.get_channel(655195773830430776)
    discrim = IBot.user.name + '#' + IBot.user.discriminator
    embed = discord.Embed(title="Logging",
                          description="Startup", color=0xffffff)
    embed.set_thumbnail(url="https://i.imgur.com/uIXcXbM.png")
    embed.add_field(name="Ready",
                    value=f"Logged in as: {discrim}",
                    inline=False)
    embed.add_field(name="Servers",
                    value=f"Total Servers: {len(IBot.guilds)}",
                    inline=True)
    embed.add_field(name="Login",
                    value=f"Login URL: {discord.utils.oauth_url(client_id)}",
                    inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    await logchan.send(embed=embed)


# Commands


@IBot.command()
async def ping(ctx):
    await ctx.send('Pong!.')
    await logging('Command Used', 'Ping', ctx)


@IBot.command()
async def purge(ctx, amount: int):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if amount is None:
                await ctx.send('You must input an amount.')
            else:
                deleted = await ctx.message.channel.purge(limit=amount)
                await ctx.send(f'Purged {len(deleted)} messages.')
                await asyncio.sleep(0.25)
                await ctx.send(f'Purged By {ctx.author}.')
        except Exception:
            await ctx.send('Command Failed: Bot has Insufficent Permissions.')
            raise
    else:
        await ctx.send('Command Failed: Insufficent Permissions.')


@IBot.command()
async def gulag(ctx, user: discord.Member, *, reason=None):
    if user.guild_permissions.manage_messages:
        await ctx.send('Command failed: Cannot target staff.')
    elif ctx.message.author.guild_permissions.manage_roles:
        if reason is None:
            await ctx.send('Must Supply a Reason:')
        else:
            role = discord.utils.get(ctx.guild.roles, name='Untermensch')
            await user.add_roles(role)
            await ctx.send(f'{user} has been Gulag\'d by {ctx.author}')


@IBot.command()
async def pardon(ctx, user: discord.Member, *, reason=None):
    if user.guild_permissions.manage_messages:
        await ctx.send('Command failed: Cannot target staff.')
    elif ctx.message.author.guild_permissions.manage_roles:
        if reason is None:
            await ctx.send('Must Supply a Reason:')
        else:
            role = discord.utils.get(ctx.guild.roles, name='Untermensch')
            await user.remove_roles(role)
            await ctx.send(f'{user} has been Pardon\'d by {ctx.author}')
IBot.run(token, bot=True)
