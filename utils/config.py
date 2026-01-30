import os
import json

ENV = os.getenv("ENV", "uat")      # qa / uat / prod
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
env_file_path = os.path.join("env", f"{ENV}.json")

with open(env_file_path) as f:
    env_config = json.load(f)
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 10
