FROM revotech2017/wi-python-ai-facies:latest

COPY . /app

WORKDIR /app

CMD ["python3", "index.py"]