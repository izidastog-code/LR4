FROM python:3.11-slim

WORKDIR /requests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY request_generator.py .

CMD ["python", "request_generator.py"]

# docker build -t request-generator:1 .
# docker run --rm request-generator:1
