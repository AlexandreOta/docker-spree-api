FROM python:3

ADD . /carga
ADD . /spree

WORKDIR /carga

RUN pip3 install -r requirements.txt






