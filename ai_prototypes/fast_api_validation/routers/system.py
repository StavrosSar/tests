#Health and echo with logs
import logging
from fastapi import APIRouter
from schemas.echo import EchoPayload

logger = logging.getLogger("app")

router = APIRouter(tags=["system"])

@router.get("/health")
def health():
    logger.info("health_check", extra={"endpoint": "/health"})
    return {"status": "ok"}

@router.post("/echo")
def echo(payload: EchoPayload):
    logger.info("echo", extra={"endpoint": "/echo", "message": payload.message})
    return payload
