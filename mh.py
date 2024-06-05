import discord
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

#load token from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

#start discord client
intents = discord.Intents.default()
intents.guild_messages = True

client = discord.Client(intents=intents)

#user_input = input("Enter a monster name: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

    
def get_monster_url(user_input):

    monsters = requests.get('https://mhworld.kiranico.com/es/monsters', headers=headers)

    soup = BeautifulSoup(monsters.text, 'html.parser')
    monsters = soup.find("a", href=lambda href: href and user_input in href)

    monster_link = monsters.get('href')
    

    return monster_link

def get_monster_droprates(user_input):

    droprate = requests.get(get_monster_url(user_input))

    soup = BeautifulSoup(droprate.text, 'html.parser')

    #TODO Find a way to list beyond low rank and get parents

    carved = soup.find('td', string='Cortados').parent.parent
    tail_carved = soup.find('td', string='Cola: cortable').parent.parent
    dropped_material = soup.find('td', string='Material caído').parent.parent
    bandit_mantel = soup.find('td', string='Manto de bandido').parent.parent
    plunderblade = soup.find('td', string='Cortabolsas').parent.parent
    palicos = soup.find('td', string='Objetos recogidos por camaradas').parent.parent


@client.event
async def on_ready():
    print('Logged in')



@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    await message.channel.send('test')
    

client.run(DISCORD_TOKEN)