import os
from celery import Celery
from dotenv import load_dotenv
from app.services.llm_analyzer import analyze_with_llm

load_dotenv()
celery_app = Celery("worker", broker=os.getenv("REDIS_URL"))

@celery_app.task
def analyze_code_task(code: str):
    return analyze_with_llm(code)