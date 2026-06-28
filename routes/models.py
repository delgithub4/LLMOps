from fastapi import APIRouter

from services.llm_service import LLMService

router = APIRouter(
    prefix="/models",
    tags=["Models"]
)

service = LLMService()


@router.get("/")
def models():

    return service.overview()
