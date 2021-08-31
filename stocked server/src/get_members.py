# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


from datetime import datetime


def get_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y - %H:%M:%S:\n\n")



token = "token"
id = 856585757984817212

invalid = """\/:*?"<>|’ !.&%"'"""


intents = discord.Intents.all()
intents.members = True



ghoul = commands.Bot(command_prefix= "ghoul", description= "ghoul", intents=intents)


def content_type(file):
    return file.filename.split('.')[-1]


members = []


def clean(username: str):
    for char in invalid:
        username = username.replace(char, "")
    return "".join(a.lower() for a in username)



@ghoul.event
async def on_ready():
    global user_logs

    guild = ghoul.get_guild(id)
    members = guild.members
    for member in members:
        
        stmember = str(member).split("#")[0]
        m = clean(stmember)
        print(m, "{}/{}".format(members.index(member)+1, len(members)))
        trname = str(member)
        trid = str(member.id)
        with open('db/'+m+".txt", 'w', encoding='utf-8') as f:
            f.write(get_time() + "Discord Username: " + trname + "\nDiscord ID: " + trid + "\nMember of discord.gg/plague.")
    input("Done!")



ghoul.run(token)
