FROM python:3.10

EXPOSE 5000

WORKDIR /app

# RUN pip install flask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# COPY . /app # this could be an alternative

CMD ["flask", "run", "--debug","--host", "0.0.0.0"]

