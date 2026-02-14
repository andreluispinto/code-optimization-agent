from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base

class AnalysisHistory(Base):
    __tablename__ = "analysis_history"
<<<<<<< HEAD
=======

>>>>>>> 7c061421991884afade067f7e9a3706e362c231d
    id = Column(Integer, primary_key=True, index=True)
    code_snippet = Column(Text, nullable=False)
    suggestions = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())