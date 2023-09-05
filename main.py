from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}


@app.get("/Poroto")
def poroto_gordo():
    return {"message": "Poroto esta bien waton"}