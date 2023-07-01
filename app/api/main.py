import utils

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

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

@app.get("/api/v1.0/predict/{caption}", tags=["ai"])
def crear_posteo(caption: str):
    # img_data = model.predict(input_data.text)
        # Crear una imagen PIL desde el arreglo NumPy
    img_data = 0
    stream = utils.create_stream(img_data)

    # Return generate image as stream io.Byte array
    return StreamingResponse(stream, media_type="image/jpeg")


if __name__ == "__main__":
    # Server start
    uvicorn.run('main:app', host="0.0.0.0", port=5000, reload=True)