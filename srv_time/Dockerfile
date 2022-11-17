FROM python:3.8-slim

WORKDIR /home/app

COPY ./srv_time/requirements.txt /home/app/requirements.txt

RUN pip3.8 install --upgrade pip && pip3.8 install -r requirements.txt

COPY ./srv_time /home/app

CMD [ "python3.8", "-u", "main.py" ]