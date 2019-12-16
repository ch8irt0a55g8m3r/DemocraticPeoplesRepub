import discord
from discord.ext import commands
import asyncio
import pprint

token = '(REDACTED)'
Spy = commands.Bot(command_prefix='>)', case_insensitive=True)


@Spy.event
async def on_ready():
    print('Online')


@Spy.event
async def on_message(message):
    target = Spy.get_guild(616669879520460804)
    home = Spy.get_channel(655961897425960970)
    if message.guild == target:
        print(message.guild.name)
        print(message.channel.name)
        print(message.author)
        print(message.content)
        # await home.send(f'''{message.guild.name} {message.channel.name}
        #    {message.author}:
        #    {message.content}''')
        embed = discord.Embed(title=message.channel.name,
                              description=message.author.name)
        embed.set_author(name=message.guild.name,
                         icon_url=message.guild.icon_url)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="Content", value=message.content, inline=False)
        await home.send(embed=embed)
        await asyncio.sleep(0.21)
    await Spy.process_commands(message)


@Spy.command()
async def userdatamine(ctx, server: int):
    target = Spy.get_guild(server)
    home = Spy.get_channel(655990488805146641)
    await ctx.send(f'Guild Aquired: {target.name}')
    pprint.pprint(target.members)
    for i in target.members:
        targetmember = await Spy.fetch_user_profile(i.id)
        if not targetmember.connected_accounts:
            continue
        else:
            await home.send(f'''{targetmember.user.name}#{targetmember.user.discriminator}
{targetmember.connected_accounts}''')
        await asyncio.sleep(0.51)


@Spy.command()
async def massmess(ctx, server: int):
    target = Spy.get_guild(server)
    for i in target.members:
        targetuser = await Spy.fetch_user(i.id)
        pprint.pprint(targetuser)
Spy.run(token, bot=False)
