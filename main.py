from fastapi import FastAPI
app = FastAPI()

@app.get("/items/")
def suma(a:int, b:int):
    return a+b