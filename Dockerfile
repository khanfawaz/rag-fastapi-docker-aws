# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc poppler-utils libmagic-dev curl git tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]