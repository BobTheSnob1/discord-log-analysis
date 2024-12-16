import json
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt


file_paths = ["announcements.json", "event-news.json"]

for file_path in file_paths:
    plt.clf()
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    timestamps = [msg["timestamp"] for msg in data.get("messages", [])]

    weekdays = [datetime.fromisoformat(ts).strftime("%A") for ts in timestamps]
    weekday_counts = Counter(weekdays)

    ordered_weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    ordered_counts = [weekday_counts.get(day, 0) for day in ordered_weekdays]
    plt.bar(ordered_weekdays, ordered_counts)
    plt.title("Messages Sent Per Weekday in #" + file_path.split(".")[0])
    plt.xlabel("Weekday")
    plt.ylabel("Number of Messages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(file_path.split(".")[0] + "_weekday_distribution.png")
    # Messages per month over the last 12 months
    plt.clf()
    current_date = datetime.now()
    last_12_months = [(current_date.year, current_date.month - i) for i in range(12)]
    last_12_months = [(y, m + 12) if m <= 0 else (y, m) for y, m in last_12_months]
    last_12_months.reverse()

    month_years = [datetime(y, m, 1).strftime("%Y-%m") for y, m in last_12_months]
    month_counts = Counter(
        datetime.fromisoformat(ts).strftime("%Y-%m") for ts in timestamps
    )

    ordered_month_counts = [month_counts.get(month, 0) for month in month_years]
    plt.bar(month_years, ordered_month_counts)
    plt.title("Messages Sent Per Month in #" + file_path.split(".")[0])
    plt.xlabel("Month")
    plt.ylabel("Number of Messages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(file_path.split(".")[0] + "_monthly_distribution.png")
    # Sum of messages per weekday for both files
    plt.clf()
    total_weekday_counts = Counter()

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        timestamps = [msg["timestamp"] for msg in data.get("messages", [])]
        weekdays = [datetime.fromisoformat(ts).strftime("%A") for ts in timestamps]
        weekday_counts = Counter(weekdays)
        total_weekday_counts.update(weekday_counts)

    ordered_counts = [total_weekday_counts.get(day, 0) for day in ordered_weekdays]
    plt.bar(ordered_weekdays, ordered_counts)
    plt.title("Total Messages Sent Per Weekday")
    plt.xlabel("Weekday")
    plt.ylabel("Number of Messages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_weekday_distribution.png")

    # Sum of messages per month for both files
    plt.clf()
    total_month_counts = Counter()

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        timestamps = [msg["timestamp"] for msg in data.get("messages", [])]
        month_counts = Counter(
            datetime.fromisoformat(ts).strftime("%Y-%m") for ts in timestamps
        )
        total_month_counts.update(month_counts)

    ordered_month_counts = [total_month_counts.get(month, 0) for month in month_years]
    plt.bar(month_years, ordered_month_counts)
    plt.title("Total Messages Sent Per Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Messages")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_monthly_distribution.png")