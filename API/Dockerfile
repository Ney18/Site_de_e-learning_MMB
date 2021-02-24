FROM python:latest

WORKDIR /flask

EXPOSE 4002

COPY ./.

RUN pip flask install mysql-connector-python

CMD ["python", "api_flask.py"]