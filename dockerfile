FROM python:3.10

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

CMD ["uvicorn", "src.web.server:app", "--host", "0.0.0.0", "--port", "8000"]