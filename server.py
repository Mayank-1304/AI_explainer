from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

# Load variables before importing router
load_dotenv()

from routers import explain

app = FastAPI()

# Resolve Paths relative to file inside module
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")

# Mount Static
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include Router
app.include_router(explain.router)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join(static_dir, "index.html"), "r") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
