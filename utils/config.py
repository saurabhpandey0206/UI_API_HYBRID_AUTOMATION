import os
from dotenv import load_dotenv

# Load .env only if it exists (local runs)
if os.path.exists("configs/env.env"):
    load_dotenv("configs/env.env")

BASE_URL = os.getenv("BASE_URL")
LOGIN_URL = os.getenv("LOGIN_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
