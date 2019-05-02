FROM revotech2017/wi-python-node:latest

RUN apk install pkg-config -y 

RUN pip3 install  matplotlib seaborn pywt statsmodels flask

COPY . /app

WORKDIR /app


CMD ["python3", "index.py"]


