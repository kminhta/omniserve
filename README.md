# Local Model Server

A lightweight FastAPI server serving a single PyTorch model locally.  
Supports simple stateless inference via the `/infer` endpoint.

---

## Run the server

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Repo Structure

```
.
├─ README.md
├─ requirements.txt
├─ train.py
├─ model/
│  └─ model.pt                 # pretrained model
├─ app/
│  ├─ main.py                  # FastAPI app with /infer endpoint
│  └─ utils.py                 # preprocessing/postprocessing helpers
└─ tests/
   └─ test_inference.py        # simple test script
```