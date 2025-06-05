import os
import json
import pandas as pd

PLAYER_NAME = "yayo"
TAG = "adios"
MATCH_PATH = "data/raw/matches/"

records = []

for file in os.listdir(MATCH_PATH):
    with open(os.path.join(MATCH_PATH, file), "r") as f:
        match = json.load(f)

    participants = match["info"]["participants"]

    for p in participants:
        if p.get("riotIdGameName", "").lower() == PLAYER_NAME and p.get("riotIdTagline", "").lower() == TAG:
            c = p.get("challenges", {})  # evitar error si no existe

            record = {
                "match_id": match["metadata"]["matchId"],
                "champion": p["championName"],
                "role": p["teamPosition"],
                "lane": p["lane"],
                "kills": p["kills"],
                "deaths": p["deaths"],
                "assists": p["assists"],
                "win": p["win"],
                "goldEarned": p["goldEarned"],
                "cs": p["totalMinionsKilled"] + p["neutralMinionsKilled"],
                "duration_min": match["info"]["gameDuration"] / 60,

                # Métricas de estilo de juego
                "killParticipation": c.get("killParticipation"),
                "soloKills": c.get("soloKills"),
                "teamDamagePercentage": c.get("teamDamagePercentage"),
                "damagePerMinute": c.get("damagePerMinute"),
                "goldPerMinute": c.get("goldPerMinute"),
                "visionScorePerMinute": c.get("visionScorePerMinute"),
                "controlWardsPlaced": c.get("controlWardsPlaced"),
                "timeSpentInEnemyHalf": c.get("timeSpentInEnemyHalf"),
                "turretTakedowns": c.get("turretTakedowns"),
                "teleportsCompleted": c.get("teleportsCompleted"),
                "longestTimeSpentLiving": c.get("longestTimeSpentLiving"),
                "timeCCingOthers": p.get("timeCCingOthers"),
                "wardsKilled": p.get("wardsKilled"),
                "wardsPlaced": p.get("wardsPlaced")
            }
            records.append(record)

df = pd.DataFrame(records)
print(df.head())
df.to_csv("data/yayo_detailed_stats.csv", index=False)