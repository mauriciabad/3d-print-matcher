FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./requirements_background.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt

COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt

WORKDIR /app/background
RUN echo "u2net" | ./setup.sh

WORKDIR /app
ENTRYPOINT ["./run.sh"]
