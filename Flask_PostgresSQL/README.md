# Flask App with PostgreSQL

This is a simple Flask application that uses PostgreSQL as its database.

## Create .env file

Create a `.env` file in the root directory of the project with the following content:

```
DB_USER=CHANGE_ME
DB_PASSWORD=CHANGE_ME
DB_HOST=CHANGE_ME
DB_PORT=CHANGE_ME
DB_DATABASE=CHANGE_ME
```

## Running locally

```python
pip install pipenv
pipenv shell
pipenv install
python app.py
```

### Using Docker

```docker
docker compose up
```

## References

https://youtu.be/Qqgry8mezC8?si=jx-kHzJ179iMkeqX
https://github.com/FaztWeb/flask-postgres-crud-spa
