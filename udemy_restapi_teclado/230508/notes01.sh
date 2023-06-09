
python -m venv .venv
source .venv/bin/activate
pip install black mypy
pip install flask 

touch app.py

# how to run the flask app
flask run --debug

touch Dockerfile

docker build -t williamszk/rest-api-flask-python .

docker run --rm -p 5000:5000 --name rest-api-flask-python williamszk/rest-api-flask-python

docker kill rest-api-flask-python
docker rm rest-api-flask-python


