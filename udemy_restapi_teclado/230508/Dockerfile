FROM python:3.10

EXPOSE 5000

WORKDIR /app

RUN pip install flask

COPY . .
# COPY . /app # this could be an alternative

CMD ["flask", "run", "--host", "0.0.0.0"]

