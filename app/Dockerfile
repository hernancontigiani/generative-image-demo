FROM python:3.10.6

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /opt/api

COPY api/ .

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload