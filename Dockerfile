FROM python:latest

WORKDIR /app

EXPOSE 5000

ENV FLASK_APP=api_flask.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN pip install --no-cache-dir -r file/requirements.txt

CMD ["flask", "run"]