# Model Server (FastAPI + Docker)

A lightweight FastAPI server serving a single PyTorch model.  
Supports simple stateless inference via the `/infer` endpoint.  
Can be run **locally** or **containerized with Docker**.

---

##  Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Test Endpoints

Health check
```bash
curl http://localhost:8000/health
```

Inference
```
curl -X POST "http://localhost:8000/infer" \
  -H "Content-Type: application/json" \
  -d '{"inputs": [[1.0], [2.0], [3.0]]}'
```

## Run with Docker
### Build & Run (standalone)
```bash
docker build -t model-server .
docker run -p 8000:8000 model-server
```

### Run with Docker Compose
```bash
docker-compose up --build
```

By default, the model/ directory is mounted into the container,
so you can update model.pt without rebuilding the image.

## Repo Structure

```
.
├─ Dockerfile
├─ docker-compose.yml
├─ README.md
├─ requirements.txt
├─ model/
│  └─ model.pt                 # pretrained model
├─ app/
│  ├─ main.py                  # FastAPI app with /health and /infer endpoints
│  └─ utils.py                 # preprocessing/postprocessing helpers
└─ tests/
   └─ test_inference.py        # simple test script

```