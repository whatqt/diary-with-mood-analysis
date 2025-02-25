from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app_index = FastAPI()

@app_index.get("/")
async def index(request: Request):
    json_data = jsonable_encoder(
        {"message": "index page"}
    )
    return JSONResponse(json_data)