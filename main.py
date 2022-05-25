# Python
from typing import Optional

# FastApi
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

# code

import services.conversion_service as conversion_service 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/conversion")
def rate_conversion(org: str = Query(...,min_length=3, max_length=3), 
                    dest: str = Query(...,min_length=3, max_length=3),
                    amount: int = Query(..., gt=0)
                    ):

    return {"data": conversion_service.get_conversion(org,dest,amount)}
