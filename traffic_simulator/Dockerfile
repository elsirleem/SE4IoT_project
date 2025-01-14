FROM python:3.12-slim

WORKDIR /app

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY python_simulation.py .
COPY config.ini .

CMD ["python", "-u", "python_simulation.py"]
