<<<<<<< HEAD
from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine

app = FastAPI(title="Enterprise Code Optimization Agent")
Base.metadata.create_all(bind=engine)
=======
from fastapi import FastAPI 
from app.api.routes import router
from app.db.database import Base, engine

app = FastAPI(title="Code Optimization Agent")

Base.metadata.create_all(bind=engine)

>>>>>>> 7c061421991884afade067f7e9a3706e362c231d
app.include_router(router)