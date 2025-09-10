FROM python:3.10-slim

# Install system dependencies required by torch/numpy
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first (for caching layers)
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ app/
COPY model/ model/

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with uvicorn (reload disabled in container)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
