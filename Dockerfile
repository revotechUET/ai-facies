FROM python:3.7-alpine

RUN apk update 

RUN pip3 install pipenv

COPY . /app

WORKDIR /app

RUN pipenv install 

RUN pipenv shell

CMD ["python3", "index.py"]


