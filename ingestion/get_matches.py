
import requests
import os

API_KEY = os.getenv("RIOT_API_KEY")
REGION = "la1"         # región para summoner info
MATCH_REGION = "americas"  # región para historial de partidas

SUMMONER_NAME = "yayo"
TAG = "adios"

# 1. Obtener PUUID del jugador

url_puuid = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{SUMMONER_NAME}/{TAG}"
headers = {"X-Riot-Token": API_KEY}
res = requests.get(url_puuid, headers=headers)

if res.status_code == 200:
    summoner = res.json()
    PUUID = summoner["puuid"]
    print("PUUID:", PUUID)
else:
    print("Error:", res.status_code)
    exit()

# 2. Obtener IDs de partidas recientes
url_matches = f"https://{MATCH_REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?count=10"
res_matches = requests.get(url_matches, headers=headers)

if res_matches.status_code == 200:
    match_ids = res_matches.json()
    print("Partidas recientes:")
    for match in match_ids:
        print(match)
else:
    print("Error al obtener partidas:", res_matches.status_code)
