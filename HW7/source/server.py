from typing import Union
import requests

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()
    print(target)
    print(method)
    print(headers)
    print(payload)
    print('----------')
    if headers:
        for header in headers:
            header_name = header.split(':')[0]
            header_value = header.split(':')[1:]
            headers_dict[header_name] = ':'.join(header_value)
    if method == "GET":
        s='http://'+target
        print(s)
        response = requests.get(s, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}")


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int):
    return JSONResponse({"item": item.dict(), "item_id": item_id})


@app.get("/")
async def homepage():
    return JSONResponse({'message': 'HELLO world'})


@app.get("/scan/")
async def scan():
    print("scan ip ")

    return JSONResponse({'ip': 'address'})

@app.get('/http/')
async def http():
    print('ok request')
    return JSONResponse({'http': 'address'})

@app.get("/get_items/{item_id}")
async def read_item(item_id: int):
    print("item_id", item_id)
    return {"item_id": item_id}
