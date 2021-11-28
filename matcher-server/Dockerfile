FROM python:3.8

# RUN useradd -ms /bin/bash harambe
# USER harambe

COPY ./requirements_background.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt

COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt

# USER root
# RUN chown -R harambe .
# USER harambe

WORKDIR /app/background
RUN echo "u2net" | ./setup.sh

# USER root
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# USER harambe

WORKDIR /app
ENTRYPOINT ["./run.sh"]
