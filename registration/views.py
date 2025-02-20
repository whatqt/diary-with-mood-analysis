from fastapi import FastAPI, Request, Body, Cookie
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from database.postgresql.connection import engine
from sqlalchemy.exc import IntegrityError
from .service import ManageUser, check_cookie
import random
from .test_cache import active_users



app_registration = FastAPI()

@app_registration.post("/")
async def registration(
    data = Body()
    ):
    print(data)
    username = data["username"]
    password = data["password"]

    manage_user = ManageUser(username, password)
    try:
        await manage_user.create(
        )
        return JSONResponse(
            {"status": "registered"},
            status_code=201
        )
    except IntegrityError:
        return JSONResponse(
            {"status": "Such a nickname is already occupied"},
            status_code=400
        )
    


@app_registration.post("/login")
async def log_in(data = Body()):
    username = data["username"]
    password = data["password"]
    manage_user = ManageUser(username, password)
    user = await manage_user.check()
    if user:
        response = JSONResponse({"status": "the login was completed successfully"}, 202)
        session_id = str(random.randint(10000, 99999))
        response.set_cookie(key="session_id", value=session_id)
        response.set_cookie(key="username", value=username)
        active_users[username] = {"session_id": session_id, "username": username}
        print(active_users)
        return response
    return JSONResponse({"status": "incorrect data"}, 400)


@app_registration.post("/log_out")
async def log_out(data = Body(), session_id = Cookie()):
    print("hello")
    username = data["username"]
    manage_user = ManageUser(username, ...)
    user = await manage_user.check()
    if user:
        authenticity = await check_cookie(
            session_id,
            username,
            active_users
        )
        if authenticity:
            response = JSONResponse({"status": "the log out was completed successfully"}, 202)
            del active_users[username]
            response.delete_cookie("session_id")
            response.delete_cookie("username")
            print(active_users)
            return response
        else: 
            return JSONResponse({"status": "drop"}, 406)
    return JSONResponse({"status": "you are not registered"}, 400)

