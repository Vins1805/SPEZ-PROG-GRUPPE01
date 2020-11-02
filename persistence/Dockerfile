FROM python:3

RUN pip install pymongo

WORKDIR /usr/src/app

COPY ./src/ /usr/src/app

CMD ["mongod"]