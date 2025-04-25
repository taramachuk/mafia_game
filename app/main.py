from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

hotspot_ip: str = ""

import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/test', response_class=JSONResponse)
async def reader(request: Request):
    try:
        body = await request.body()
        if not body:
            return {"error": "Empty body!"}
        data = await request.json()
        print("Received:", data)
        return {"received": data}
    except Exception as e:
        return {"error": f"Failed to parse JSON: {str(e)}"}

@app.get('/items/{item_id}')
async def read_item(item_id: Request):
    print(item_id)
    for k in globals():
        print(k)
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
