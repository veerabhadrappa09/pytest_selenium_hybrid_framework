import json
import os

ENV = os.getenv("ENV", "qa")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file_path = os.path.join(BASE_DIR, "env", f"{ENV}.json")

if not os.path.exists(env_file_path):
    raise FileNotFoundError(f"Environment file not found: {env_file_path}")

with open(env_file_path) as f:
    config = json.load(f)

BASE_URL = config["base_url"]
USERNAME = config["username"]
PASSWORD = config["password"]


IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 10


