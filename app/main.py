from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import netifaces as ni

from app.dns_server import start_dns_server
# import dns_server
# import app.dns

hotspot_ip: str = ""

interfaces = ni.interfaces()
print("Available interfaces:", interfaces)

for iface in interfaces:
    try:
        netia = "{1D86853C-6162-4A36-A424-00B994BC2B13}"
        local = "{1F3FDF89-60DA-4EE4-B725-B2B3215D2CA8}"
        hotspot_name = "ap_br_wlan2"
        addrs = ni.ifaddresses(iface)
        if ni.AF_INET in addrs:
            print(f"Interface {iface} IP:", addrs[ni.AF_INET][0]['addr'])
        
        if iface == hotspot_name:
            hotspot_ip = addrs[ni.AF_INET][0]['addr']
            print("HOTSPOT IP :", hotspot_ip)
        
        if iface == local:
            print(iface)
            print(f"Interface {iface} MAFIA IP:", addrs[ni.AF_INET][0]['addr'])

    except Exception as e:
        print(f"Error on interface {iface}:", e)

if hotspot_ip:
    start_dns_server(hotspot_ip)

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
