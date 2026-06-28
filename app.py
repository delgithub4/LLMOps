from fastapi import FastAPI

from routes.models import router as model_router
from routes.health import router as health_router

app = FastAPI(
    title="LLMOps",
    version="1.0.0"
)

app.include_router(model_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"LLMOps",

        "status":"running"

    }
