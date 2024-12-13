import json
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt


file_paths = ["announcements.json", "event-news.json"]

for file_path in file_paths:
    plt.clf()
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    timestamps = [msg['timestamp'] for msg in data.get('messages', [])]

    weekdays = [datetime.fromisoformat(ts).strftime('%A') for ts in timestamps]
    weekday_counts = Counter(weekdays)

    ordered_weekdays = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday'
    ]
    ordered_counts = [weekday_counts.get(day, 0) for day in ordered_weekdays]
    plt.bar(ordered_weekdays, ordered_counts)
    plt.title("Messages Sent Per Weekday in #" + file_path.split(".")[0])
    plt.xlabel("Weekday")
    plt.ylabel("Number of Messages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(file_path.split(".")[0] + "_weekday_distribution.png")
