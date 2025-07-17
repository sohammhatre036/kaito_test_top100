import requests
import json
import os

def fetch_kaito_leaderboard(topic_id, duration, subfolder):
    url = "https://hub.kaito.ai/api/v1/gateway/ai/kol/mindshare/top-leaderboard"
    params = {
        'duration': duration,
        'topic_id': topic_id,
        'top_n': 200,  # 🔧 Set to 200 users
        'customized_community': 'customized',
        'community_yaps': True
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    try:
        print(f"🔄 Fetching data for topic: {topic_id} | duration: {duration}")
        folder_path = os.path.join("kaito_data", subfolder)
        os.makedirs(folder_path, exist_ok=True)

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            file_path = os.path.join(folder_path, f"data_{topic_id}_{duration}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Saved to '{file_path}' ({len(data)} records)")
        else:
            print(f"❌ Failed for {topic_id} {duration} | Status: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"❌ Error for {topic_id} {duration}: {e}")


if __name__ == "__main__":
    print("🚀 Fetching Kaito Leaderboard Data...")
    print("=" * 40)

    durations = ['7d', '30d', '3m', '6m']

    topics = {
        "HANAHANA": "hanahana",
        "ANOMA": "anoma",
        "BLS": "bls"
    }

    for topic_id, folder in topics.items():
        for duration in durations:
            fetch_kaito_leaderboard(topic_id, duration, folder)

    print("\n✅ All data fetched successfully!")
