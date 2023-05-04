# https://www.youtube.com/watch?v=uoJ6OwlSOWg&ab_channel=TejaWithData

# we assume that the name of the app file is:
# my_app.py
gunicorn --workers=5 --bind 0.0.0.0:5000 my_app:app
