FROM revotech2017/wi-python-ai-facies:latest

COPY . /app

WORKDIR /app

RUN pip3 install --no-cache-dir flask-cors

CMD ["python3", "index.py"]