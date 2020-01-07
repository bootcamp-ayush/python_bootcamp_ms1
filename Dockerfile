FROM python:3.7-alpine3.9
EXPOSE 8080
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk update &&\
  apk add curl


ENTRYPOINT [ "python3" ]
CMD ["wsgi.py"]
