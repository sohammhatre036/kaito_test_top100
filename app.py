from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def fetch_kaito_data(topic, duration):
    try:
        folder = "kaito_data" if topic == "HANAHANA" else "kaito_data_anoma"
        file_path = os.path.join(folder, f"data_{topic}_{duration}.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data[:100]  # Top 100
    except Exception as e:
        print(f"Error loading {topic} {duration} data: {e}")
        return []

@app.route("/")
def index():
    # Defaults
    duration = request.args.get('duration', '7d')
    topic = request.args.get('topic', 'HANAHANA')

    # Fetch users
    users = fetch_kaito_data(topic, duration)

    return render_template(
        "index.html",
        users=users,
        duration=duration,
        topic=topic,
        durations=['7d', '30d', '3m', '6m'],
        topics=['HANAHANA', 'ANOMA']
    )

if __name__ == "__main__":
    app.run(debug=True)
