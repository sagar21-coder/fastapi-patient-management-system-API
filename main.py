from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def hello():
    return{'message':'Patient Management System API'}

@app.get("/about")
def about():
    return{'message':'A fully functional API to manage your patients records'}
    