from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import requests
import torch

app = FastAPI()

@app.get('/')
async def index():
 return {'message':'Hello,World'}

@app.get('/{name}')
async def get_name(name: str):
 return {'Welcome To Here': f'{name}'}
