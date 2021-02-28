FROM python:latest

WORKDIR /flask

EXPOSE 5000

ENV FLASK_APP=development

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN pip install flask mysql-connector-python jinja

CMD ["flask", "run"]