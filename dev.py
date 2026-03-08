from fastapi.staticfiles import StaticFiles
from api.index import app
import uvicorn
import os

# Create a small development server that serves both the API and the static files
# Since FastAPI matches explicitly defined routes before mounted apps,
# the /api/generate route will continue to work while serving index.html on /

app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    print("Starting local development server at http://127.0.0.1:8000 ...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
