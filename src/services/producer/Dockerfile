FROM python:3.11-slim
LABEL authors="ispaneli"

WORKDIR /app

COPY requirements.txt .
COPY /src /app/src

RUN pip install --upgrade pip wheel setuptools && \
    pip install -r requirements.txt
# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "src/main.py"]
