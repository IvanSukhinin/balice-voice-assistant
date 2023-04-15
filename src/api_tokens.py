import json

with open('api_tokens.json', 'r') as f:
	tokens = json.load(f)

CHAT_GPT_TOKEN = tokens['CHAT_GPT_TOKEN']
OPEN_WEATHER_TOKEN = tokens['OPEN_WEATHER_TOKEN']
