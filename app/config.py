import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:

    MODELS_DIR = os.path.join(BASE_DIR, "../models")
    PERSONALITY_FILE = os.path.join(BASE_DIR, "personalities", "default.json")

    # Load personality info
    @staticmethod
    def load_personality():
        if not os.path.exists(Config.PERSONALITY_FILE):
            return {}
        with open(Config.PERSONALITY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
