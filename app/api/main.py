import utils

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from schemas import PredictSchema

# Create model
# from ai import StableDiffusion
# model = StableDiffusion()
# model.build_model()

# Create server
app = FastAPI(
    title="DiffusionAPI",
    version="1.0.0",
    )

# CORS config
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# ------------ Views -------------------------- #
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---------------- API ------------------------ #

@app.post("/api/v1.0/predict", tags=["ai"])
def crear_posteo(input_data: PredictSchema):
    # img_data = model.predict(input_data.text)
    img_data = "asdasd"
    return {"inference": img_data}


if __name__ == "__main__":
    # Server start
    uvicorn.run('main:app', host="0.0.0.0", port=5000, reload=True)