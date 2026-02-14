<<<<<<< HEAD
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.cache import get_cache, set_cache
from app.tasks.worker import analyze_code_task
from app.db.database import SessionLocal
from app.db.models import AnalysisHistory
from prometheus_client import Counter

router = APIRouter()
REQUEST_COUNT = Counter("analyze_requests_total", "Total analyze requests")
=======
from fastapi import APIRouter, HTTPException
from app.services.analyzer import analyze_code_logic
from app.db.models import AnalysisHistory
from app.db.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()
>>>>>>> 7c061421991884afade067f7e9a3706e362c231d

class CodeRequest(BaseModel):
    code_snippet: str

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/analyze-code")
def analyze_code(request: CodeRequest):
<<<<<<< HEAD
    REQUEST_COUNT.inc()
    cache_key = f"analysis:{hash(request.code_snippet)}"
    cached = get_cache(cache_key)
    if cached:
        return {"suggestions": cached.decode()}

    task = analyze_code_task.delay(request.code_snippet)
    suggestions = task.get()

    set_cache(cache_key, suggestions)

    db = SessionLocal()
    record = AnalysisHistory(code_snippet=request.code_snippet, suggestions=suggestions)
    db.add(record)
    db.commit()
    db.close()

    return {"suggestions": suggestions}
=======
    suggestions = analyze_code_logic(request.code_snippet)
    
    db = SessionLocal()
    record = AnalysisHistory(
        code_snippet=request.code_snippet,
        suggestions=suggestions
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return {
        "analysis_id": record.id,
        "suggestions": suggestions
    }
>>>>>>> 7c061421991884afade067f7e9a3706e362c231d
