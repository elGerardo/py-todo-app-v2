FROM python:3.9

WORKDIR /home/node/app

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt


EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
