import json
import os

def load_knowledge():
    file_path = os.path.join(os.path.dirname(__file__), "knowledge.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data



