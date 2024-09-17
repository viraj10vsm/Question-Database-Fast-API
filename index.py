from fastapi import FastAPI
from routes.question import question 
app = FastAPI()
app.include_router(question)