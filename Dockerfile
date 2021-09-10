FROM python:3.8-slim

WORKDIR /home/simpleflaskapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY simpleflaskapp.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP simpleflaskapp.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]