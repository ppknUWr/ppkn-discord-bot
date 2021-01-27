import json

"""
TODO: Przerobić na funkcjonalnosc z read_api.py jak bedzie gotowe! 
"""
def read_data_from_private():
    with open("private/tokens.json", "r") as f:
        data = json.load(f)
        return data

tokens = read_data_from_private()

CHANNEL_ID = int(tokens["channel_id"])
SERVER_ID = int(tokens["server_id"])
TOKEN = tokens["token"]
BOT_ID = int(tokens["bot_id"])
MESSAGE_REACTION_ID = int(tokens["message_reaction_id"])