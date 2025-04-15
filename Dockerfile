# Use Python 3.11 slim image
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/ .

# Expose port and run the app
EXPOSE 5000
CMD ["python", "app.py"]
