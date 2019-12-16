#Imports
import discord
from discord.ext import commands
#import logging

#Defined Vars
token2 = '(REDACTED)'
loggingin = True
async def on_message(message):
    author = message.author
    content = message.content
    print('###')
    print(author, "said: ")
    print(" ", content)
    print('###')
    print()

async def login():
  if loggingin == True:
    await login(token2)
login()
