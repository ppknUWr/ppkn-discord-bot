# json z przywitanymi to_jest_funkcja()
from discord import Client
import json

async def welcome(user):
    with open("members.json", "r") as file:     # otwiera plik do odcztu
        users_match = json.load(file)           # pobiera wartosci z pliku
        print(users_match)
    if user.id not in users_match:       # jesli nie znajdzie
        channel = await user.create_dm()        # to wysle wiadomosc
        await channel.send("Witaj u nas na serwerze " + user.name)
        users_match[user.name] = user.id
    with open("members.json", "w") as file:     # nadpisuje liste
        json.dump(users_match, file, indent=4)

