from fastapi import FastAPI, Query
from routers.items import router as items_router
from routers.system import router as system_router
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")

app = FastAPI()

app.include_router(items_router)
app.include_router(system_router)

# Root endpoint
#Altered
@app.get("/")
def root(a: int = Query(0), b: int = Query(0)):
    # Adds two numbers provided as query parameters
    return {
        "message": "API is running",
        "a": a,
        "b": b,
        "sum": a + b
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True, #auto-restart server on code changes (DEV ONLY)
    )
