import requests
import os
import json

TOPIC_IDS = [
    "0G","ALLORA","ANOMA",
    "BLS","BOUNDLESS","CALDERA","CAMP","CYSIC",
    "FOGO","FRAX","HANAHANA","GOATNETWORK",
    "HUMANITY","INFINEX","INFINIT""IQ","IRYS","KAIA","KAT","LOMBARD",
    "LUMITERRA","MEGAETH","MEMEX","MIRA","MITOSIS","MONAD","MULTIBANK","MULTIPLI","NYT","NOYA","OPENLEDGER","PARADEX","PORTALPORTAL","PUFFPAW",
    "SATLAYER","SIDEKICK","SOMNIA","SO","SUCCINCT","SURF","SYMPHONY","THEORIQ","THRIVE","TURTLECLUB","UNION"
    ,"YEET","ZEC"
]

# Added '12m' here
DURATIONS = ['7d', '30d', '3m', '6m', '12m']

def fetch_leaderboard(topic_id, duration):
    url = "https://hub.kaito.ai/api/v1/gateway/ai/kol/mindshare/top-leaderboard"
    params = {
        "topic_id": topic_id,
        "duration": duration,
        "top_n": 200,
        "customized_community": "customized",
        "community_yaps": True
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    folder = os.path.join("kaito_data", topic_id.lower())
    os.makedirs(folder, exist_ok=True)

    try:
        print(f"🔄 Fetching {topic_id} | {duration}")
        response = requests.get(url, params=params, headers=headers)
        if response.ok:
            data = response.json()
            file_path = os.path.join(folder, f"data_{topic_id}_{duration}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Saved: {file_path} ({len(data)} records)")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Exception fetching {topic_id} {duration}: {e}")

if __name__ == "__main__":
    print("🚀 Fetching Kaito Leaderboard Data...\n" + "=" * 40)
    for topic_id in TOPIC_IDS:
        for duration in DURATIONS:
            fetch_leaderboard(topic_id, duration)
    print("\n✅ All done!")
