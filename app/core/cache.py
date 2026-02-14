import os
import redis
from dotenv import load_dotenv

load_dotenv()
redis_client = redis.from_url(os.getenv("REDIS_URL"))

def get_cache(key: str):
    return redis_client.get(key)

def set_cache(key: str, value: str, ttl: int = 3600):
    redis_client.setex(key, ttl, value)