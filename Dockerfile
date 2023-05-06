FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/app.py /app
COPY ./src/helpers.py /app

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--workers", "1", "--port", "80"]
