FROM python:3.10.14-slim
WORKDIR /app

COPY ./__install__/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]

COPY . .