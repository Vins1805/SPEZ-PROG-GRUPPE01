FROM python:3

RUN pip install flask

WORKDIR /usr/src/app

COPY . .

CMD ["python","-u","server.py"]