FROM python:3.8.2-alpine3.11

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./

CMD ["gunicorn", "server:app", "-b", "0.0.0.0:8000"]
