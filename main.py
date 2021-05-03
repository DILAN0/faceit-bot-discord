import discord
import requests
from discord.ext import commands

faceit_api = "" #token faceit
ds = "" #token discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.' , intents = intents)

@bot.command()
async def faceit(ctx , nick: str):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer {}'.format(faceit_api),
    }

    params = (
        ('nickname', nick),
        ('game', 'csgo'),
    )

    response = requests.get('https://open.faceit.com/data/v4/players', headers=headers , params = params)

    data = response.json()


    if data['games']['csgo']['faceit_elo'] > 1100:
        col = 0xff9900
    if data['games']['csgo']['faceit_elo'] < 1101:
        col = 0x0015F300
    if data['games']['csgo']['faceit_elo'] > 1701:
        col = 0x00F30A0D
    if data['games']['csgo']['faceit_elo'] < 801:
        col = 0x00E8F7FF

    elo = data['games']['csgo']['faceit_elo']
    lvl = data['games']['csgo']['skill_level']
    name = data['nickname']
    avatar = data['avatar']
    player_id = data['player_id']

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer {}'.format(faceit_api),
    }

    response = requests.get('https://open.faceit.com/data/v4/players/'+player_id+'/stats/csgo',
                            headers=headers)
    data = response.json()
    kd = data["lifetime"]["Average K/D Ratio"]
    hs = data["lifetime"]["Average Headshots %"]
    winrate = data["lifetime"]["Win Rate %"]

    embed = discord.Embed(color=col, title='Stats' , description = f"ELO: {elo}\nK/D: {kd}\nHS: {hs}%\nWin Rate: {winrate}%")
    if lvl == 1:
       file = discord.File("lvl/level_1.png", filename="level_1.png")
       embed.set_author(name=name, icon_url='attachment://level_1.png')
    if lvl == 2:
        file = discord.File("lvl/level_2.png", filename="level_2.png")
        embed.set_author(name=name, icon_url='attachment://level_2.png')
    if lvl == 3:
        file = discord.File("lvl/level_3.png", filename="level_3.png")
        embed.set_author(name=name, icon_url='attachment://level_3.png')
    if lvl == 4:
        file = discord.File("lvl/level_4.png", filename="level_4.png")
        embed.set_author(name=name, icon_url='attachment://level_4.png')
    if lvl == 5:
        file = discord.File("lvl/level_5.png", filename="level_5.png")
        embed.set_author(name=name, icon_url='attachment://level_5.png')
    if lvl == 6:
        file = discord.File("lvl/level_6.png", filename="level_6.png")
        embed.set_author(name=name, icon_url='attachment://level_6.png')
    if lvl == 7:
        file = discord.File("lvl/level_7.png", filename="level_7.png")
        embed.set_author(name=name, icon_url='attachment://level_7.png')
    if lvl == 8:
        file = discord.File("lvl/level_8.png", filename="level_8.png")
        embed.set_author(name=name, icon_url='attachment://level_8.png')
    if lvl == 9:
        file = discord.File("lvl/level_9.png", filename="level_9.png")
        embed.set_author(name=name, icon_url='attachment://level_9.png')
    if lvl == 10:
        file = discord.File("lvl/level_max.png", filename="level_max.png")
        embed.set_author(name=name, icon_url='attachment://level_max.png')

    if avatar == '':
        embed.set_thumbnail(url='https://assets.faceit-cdn.net/hubs/avatar/1b588a32-e207-4596-80b9-a2ff9eabf28d_1607167905245.jpg')
    else:
        embed.set_thumbnail(url=avatar)

    await ctx.send(file = file, embed=embed)

bot.run(ds)
# этот кал можно докодить но мне лень :)