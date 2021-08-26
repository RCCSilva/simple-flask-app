FROM public.ecr.aws/sam/build-python3.8:latest

WORKDIR /home/simpleflaskapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY simpleflaskapp.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP simpleflaskapp.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]