from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOPIC_IDS = [
    "0G","ALLORA","ANOMA",
    "BLS","BOUNDLESS","CALDERA","CAMP","CYSIC",
    "FOGO","FRAX","HANAHANA","GOATNETWORK",
    "HUMANITY","INFINEX","INFINIT","IQ","IRYS","KAIA","KAT","LOMBARD",
    "LUMITERRA","MEGAETH","MEMEX","MIRA","MITOSIS","MONAD","MULTIBANK","MULTIPLI","NYT","NOYA","OPENLEDGER","PARADEX","PORTALPORTAL","PUFFPAW",
    "SATLAYER","SIDEKICK","SOMNIA","SO","SUCCINCT","SURF","SYMPHONY","THEORIQ","THRIVE","TURTLECLUB","UNION",
    "YEET","ZEC"
]

DURATIONS = ['7d', '30d', '3m', '6m', '12m']

def fetch_leaderboard(topic_id, duration, top_n=200):
    url = "https://hub.kaito.ai/api/v1/gateway/ai/kol/mindshare/top-leaderboard"
    params = {
        "topic_id": topic_id,
        "duration": duration,
        "top_n": top_n,
        "customized_community": "customized",
        "community_yaps": True
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {topic_id} {duration}: {e}")
        return []

@app.route("/")
def index():
    topic = request.args.get("topic", "HANAHANA")
    duration = request.args.get("duration", "7d")

    users = fetch_leaderboard(topic, duration, top_n=200)

    return render_template(
        "index.html",
        users=users,
        topic=topic,
        duration=duration,
        topics=TOPIC_IDS,
        durations=DURATIONS
    )

if __name__ == "__main__":
    app.run(debug=True)
