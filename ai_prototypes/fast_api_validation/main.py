from fastapi import FastAPI
from routers.items import router as items_router
from routers.system import router as system_router
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")

app = FastAPI()

app.include_router(items_router)
app.include_router(system_router)

@app.get("/")
def root():
    return {"message": "API is running"}
