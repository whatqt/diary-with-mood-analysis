from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app_introduction = FastAPI()

@app_introduction.get("/")
async def introduction(request: Request):
    json_data = jsonable_encoder(
        {"message": "introduction page"}
    )
    return JSONResponse(json_data)