import threading
import uvicorn

from app.dns_server import start_dns
from app.ip_finder import find_ip

def start_uvicorn():
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
    # uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    config = uvicorn.Config("app.main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()

if __name__ == "__main__":
    dns_ip = find_ip() 

    dns_thread = threading.Thread(target=start_dns, args=(dns_ip,), daemon=True)
    api_thread = threading.Thread(target=start_uvicorn, daemon=True)

    dns_thread.start()
    api_thread.start()

    dns_thread.join()
    api_thread.join()
