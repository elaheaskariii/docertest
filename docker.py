from fastapi import FastAPI
#1,,,,
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello! My first FastAPI project 🚀"}


@app.get("/hello")
def hello():
    return {"message": "Hello Ela!"}