from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API", description="A simple task management REST API")

app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow API. Visit /docs for API documentation."}