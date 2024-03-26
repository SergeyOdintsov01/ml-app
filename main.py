from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")


@app.get("/")
def root():
    return {"message": "This model translation text ru to eng"}


@app.get("/model")
def ml_model():
    return {"message": "ML model : Helsinki-NLP/opus-mt-ru-en"}


@app.post("/translate/")
def translate(item: Item):
    return translator(item.text)[0]


@app.post("/info")
def info():
    return {"message":"Uvicron, FastAPI, Postman"}
