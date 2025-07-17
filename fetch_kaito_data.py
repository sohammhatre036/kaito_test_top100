import requests
import json
import os

def fetch_kaito_leaderboard(topic_id, duration, folder_name):
    """
    Fetch leaderboard data for a specific topic and duration, save to specified folder.
    """
    url = "https://hub.kaito.ai/api/v1/gateway/ai/kol/mindshare/top-leaderboard"
    params = {
        'duration': duration,
        'topic_id': topic_id,
        'top_n': 1000,
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
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            os.makedirs(folder_name, exist_ok=True)
            file_path = os.path.join(folder_name, f"data_{topic_id}_{duration}.json")
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

    # HANAHANA
    for duration in durations:
        fetch_kaito_leaderboard("HANAHANA", duration, "kaito_data")

    # ANOMA
    for duration in durations:
        fetch_kaito_leaderboard("ANOMA", duration, "kaito_data_anoma")

    print("\n✅ All data fetched successfully!")
