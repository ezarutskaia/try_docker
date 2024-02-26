FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app .

EXPOSE 5555

CMD ["python", "app.py"]