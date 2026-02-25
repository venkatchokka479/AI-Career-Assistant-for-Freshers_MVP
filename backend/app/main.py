from fastapi import FastAPI

from app.api.match import router as match_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(match_router, prefix="/api/v1")


@app.get("/api/v1/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}
