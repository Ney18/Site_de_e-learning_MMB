FROM python:latest

WORKDIR /library

COPY ./.

RUN pip install mysql-connector-python bs4

CMD ["python", "docker_scrap.py"]