from contextlib import asynccontextmanager
from routers.notes import router as notes
from routers.admin import router as admin
from routers.auth import router as auth
from database import init_database
from fastapi import FastAPI, Request
from time import time
@asynccontextmanager
async def life_span(app:FastAPI):
    await init_database()
    yield

app = FastAPI(lifespan=life_span, title="Note API")

@app.middleware("http")
async def moddleware_test(request, call_next):
    begin = time()
    response = await call_next(request)
    end = time()
    print("Endpoint:", request.url.path, end-begin)
    return response

app.include_router(notes)
app.include_router(auth)
app.include_router(admin)

if __name__ == "__main__":
    from uvicorn import run
    run(app=app, host="0.0.0.0", port=8000)