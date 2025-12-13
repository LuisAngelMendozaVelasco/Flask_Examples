# Flask App with SQLite

This is a simple Flask application that uses SQLite as its database.

## Running locally

```python
pip install pipenv
pipenv shell
pipenv install
python app.py
```

### Using Docker

```docker
docker build -t flask-sqlite .
docker run -v .:/flask-app -p 5000:5000 flask-sqlite
```

## References

https://youtu.be/V9VU1g4IWlg?si=TEHF7pijEbj21I6m
https://github.com/FaztWeb/flask-sqlite3-crud