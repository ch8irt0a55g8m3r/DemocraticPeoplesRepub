import pprint
import time
import twint
import json


def discord_scrape():
    c = twint.Config()
    c.Search = "discord.gg"
    c.Limit = 100
    c.Lang = 'en'
    c.Output = 'twint.json'
    c.Store_json = True
    twint.run.Search(c)


def json_print():
    tweets = []
    flatlist = []
    for line in open('twint.json', 'r', encoding="utf8"):
        tweets.append(json.loads(line))
    urls = [r.get('urls') for r in tweets]
    for sublist in urls:
        for item in sublist:
            flatlist.append(item)
    matching = [s for s in flatlist if "discord.gg" in s]
    final = list(set(matching))
    with open("file.txt", "w") as f:
        for s in final:
            f.write(str(s) + "\n")


open('twint.json', 'w').close()
discord_scrape()
# json_print()
time.sleep(5)
print()
print('Done')
