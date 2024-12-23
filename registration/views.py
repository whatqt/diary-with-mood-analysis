from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .models import Users
from sqlalchemy.orm import Session
from database.postgresql.connection import engine
from sqlalchemy.exc import IntegrityError



app_registration = FastAPI()

@app_registration.post("/")
async def registration(
    data = Body()
    ):
    print(data)
    username = data["username"]
    password = data["password"]
    with Session(autoflush=False, bind=engine) as db:
        user = Users(
            username=username,
            password=password
        )
        db.add(user)
        try:
            db.commit()
        except IntegrityError:
            return JSONResponse(
                {"Not registered": "Such a nickname is already occupied"},
                status_code=400
            )
    
    return JSONResponse(
        {"User": "registered"},
        status_code=201
    )

@app_registration.post("/log_in")
async def log_in(data = Body()):
    pass




@app_registration.get("/log_out")
async def log_out(request: Request):
    json_data = jsonable_encoder(
        {"message": "log_out page"}
    )
    return JSONResponse(json_data)