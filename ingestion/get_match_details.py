import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
HEADERS = {"X-Riot-Token": API_KEY}
MATCH_REGION = "americas"

# Lista de match IDs que obtuviste antes
match_ids = [
    "LA1_1625147919", "LA1_1625137375", "LA1_1625123582",
    "LA1_1625117649", "LA1_1625109708", "LA1_1624697580",
    "LA1_1624683545", "LA1_1624673803", "LA1_1624668110", "LA1_1624659816"
]

# Ruta para guardar los datos
os.makedirs("data/raw/matches", exist_ok=True)

# Obtener cada partida y guardarla
for match_id in match_ids:
    url = f"https://{MATCH_REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    res = requests.get(url, headers=HEADERS)

    if res.status_code == 200:
        data = res.json()
        with open(f"data/raw/matches/{match_id}.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Guardado: {match_id}")
    else:
        print(f"❌ Error al obtener {match_id}: {res.status_code}")