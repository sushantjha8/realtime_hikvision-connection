FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER_CONTAINER 1
ENV PYTHONUNBUFFERED 1

#install cmake
RUN apt-get update && apt-get -y install cmake
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/