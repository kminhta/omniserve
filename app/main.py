from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from app.utils import preprocess, postprocess

app = FastAPI(title="Local Model Server")

MODEL_PATH = "model/model.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model once on startup
try:
    model = torch.load(MODEL_PATH, map_location=device)
    model.eval()
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

class InferenceRequest(BaseModel):
    inputs: list

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/infer")
def infer(request: InferenceRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    try:
        x = preprocess(request.dict())
        x = x.to(device)
        with torch.no_grad():
            y = model(x)
        return postprocess(y)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
