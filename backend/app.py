import joblib
from pathlib import Path

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

# create fastAPI instance
app = FastAPI()

templates = Jinja2Templates(
    directory=str(BASE_DIR.parent / "frontend" / "templates")
)

model = joblib.load(BASE_DIR.parent / "artifacts" / "lr_model.joblib")

# create pydantic data validation
class HousePriceFeatures(BaseModel):
    house_area: float

# define API endpoints
@app.get("/health")
def health():
    return {"health": "okay"}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
            name="index.html",
            request=request)

@app.post("/predict")
def predict(data: HousePriceFeatures):
    input_data = [[data.house_area]]
    price = model.predict(input_data)[0]
    return {"price": float(price)}



