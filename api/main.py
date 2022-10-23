from fastapi import FastAPI
import uvicorn 

app = FastAPI()


@app.get('/')
def hello():
    return {"Response":"Hola mundo"}

@app.get('/frutas')
def frutas():
    return {"Response":["Pera", "Manzana"] }
