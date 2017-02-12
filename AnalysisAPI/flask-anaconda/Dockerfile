FROM continuumio/anaconda:latest

MAINTAINER Vasvaroos Ngamdamrongkiat "Vasvaroos@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential libsasl2-dev libldap2-dev libssl-dev libpq-dev 

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["/code/test-api.py"]

EXPOSE 8080 5000