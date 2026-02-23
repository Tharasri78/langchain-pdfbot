import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key: str):
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Missing env variable: {key}")
    return value