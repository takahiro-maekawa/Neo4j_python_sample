FROM python:3.10.5

RUN mkdir -p /host/src
COPY requirements.txt ./
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install ipython
