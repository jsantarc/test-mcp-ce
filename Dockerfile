FROM python:3.11-slim

# Install pip and setuptools explicitly
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip setuptools

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Set environment variable for port
ENV PORT=8080

# Run the application
CMD ["python", "main.py"]
