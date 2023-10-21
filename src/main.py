from fastapi import FastAPI

import schemas
import service

app = FastAPI()


@app.get("/")
def read_root():
    return {"hi": "there"}


@app.get("/{user}/info")
def get_user(user):
# def get_user(user: schemas.User.login):
    return service.get_user(user)
