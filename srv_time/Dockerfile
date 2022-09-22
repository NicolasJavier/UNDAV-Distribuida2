FROM python:3.8-slim

COPY ./srv_time /home/app

WORKDIR /home/app

RUN pip3.8 install --upgrade pip && pip3.8 install -r requirements.txt

CMD [ "python3.8", "-u", "main.py" ]