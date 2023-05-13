python -m venv .venv

python.exe -m pip install --upgrade pip
pip install mypy 
pip install black 
pip install ipython 
pip install flask
pip install requests 
pip install types-requests
pip install pytest
pip install flask-smorest
pip install python-dotenv
pip install sqlalchemy 
pip install flask-sqlalchemy 
pip install flask_jwt_extended
pip install passlib


pip freeze > requirements.txt

# run flask
flask run

# to run flask with debug on
flask --app app.py --debug run


cd tests
pytest -sv
python3 repl_endpoints.py

# about docker
touch Dockerfile
touch .dockerignore

docker build -t rest-apis-flask-python .
docker build -t flask-smorest-api .

# run the docker container
docker run -p 5000:5000 --name my-rest-api-flask-python rest-apis-flask-python
docker run -p 5000:5000 --name my-rest-api-flask-python flask-smorest-api

docker stop my-rest-api-flask-python
docker rm my-rest-api-flask-python

# Create docker container with volume
docker run -p 5000:5000 \
    --name my-rest-api-flask-python \
    -w /app -v "$(pwd):/app" \
    flask-smorest-api

# To access the swagger-ui
http://localhost:5000/swagger-ui