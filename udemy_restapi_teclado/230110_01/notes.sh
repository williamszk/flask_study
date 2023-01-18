python -m venv .venv

pip install flask
pip install requests 
pip install types-requests
pip install pytest

# run flask
flask run

# to run flask with debug on
flask --app app.py --debug run


cd tests
pytest -sv