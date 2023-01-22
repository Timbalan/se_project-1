from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
pipe = pipeline(model="sberbank-ai/rugpt3large_based_on_gpt2")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    '''Generate text'''
    return pipe(item.text)[0]['generated_text']