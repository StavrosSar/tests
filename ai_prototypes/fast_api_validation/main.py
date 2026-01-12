from fastapi import FastAPI
from routers.items import router as items_router

app = FastAPI()

app.include_router(items_router)

@app.get("/")
def root():
    return {"message": "API is running"}
