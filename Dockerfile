FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/app.py .

EXPOSE 5555

CMD ["python", "app.py"]