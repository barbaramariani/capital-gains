FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/src

ENV PYTHONPATH "${PYTHONPATH}:/app/src"

CMD ["python", "main.py"]