from fastapi import FastAPI
from db import engine,Base
from crud import router

app= FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router,prefix='/todo')
