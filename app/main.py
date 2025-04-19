from typing import Union
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.router.auth import router as auth_router
from app.router.question import router as question_router
from app.router.option import router as option_router
from app.router.topic import router as topic_router
from app.router.participation import router as participation_router
from app.router.submission import router as submission_router
from app.router.game import router as game_router

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(auth_router)
app.include_router(question_router)
app.include_router(option_router)
app.include_router(topic_router)
app.include_router(submission_router)
app.include_router(participation_router)
app.include_router(game_router)