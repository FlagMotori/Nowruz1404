FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["gunicorn", "-w" ,"4", "-b", "0.0.0.0", "app:app"]