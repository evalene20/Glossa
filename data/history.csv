import csv
import os
from datetime import datetime

HISTORY_FILE = "data/history.csv"


def save_translation(source, target, original, translated):

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Source Language",
                "Target Language",
                "Original Text",
                "Translated Text"
            ])

        writer.writerow([
            datetime.now(),
            source,
            target,
            original,
            translated
        ])