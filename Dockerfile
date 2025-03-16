# Stage 1: Builder - Install dependencies
FROM python:3.7 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.7-slim

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/

# Copy application files
COPY . .

# Corrected ENTRYPOINT
ENTRYPOINT ["python", "run.py"]

