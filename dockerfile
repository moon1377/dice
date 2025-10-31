FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D app

USER app

EXPOSE 5000

CMD ["python", "app.py"]
