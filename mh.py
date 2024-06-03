import discord
import requests
from bs4 import BeautifulSoup

user_input = input("Enter a monster name: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
kiranico = requests.get('https://mhworld.kiranico.com/', headers=headers)
monsters = requests.get('https://mhworld.kiranico.com/es/monsters', headers=headers)

soup = BeautifulSoup(monsters.text, 'html.parser')
monsters = soup.find_all("a", href=lambda href: href and user_input in href)

for link in monsters:
    monster_link = link.get('href')
    
