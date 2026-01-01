# Flask API and React app with MongoDB 

This is a simple React App and Flask API that uses MongoDB as its database.

## Create .env file

Create a `.env` file in the root directory of the project with the following content:

```bash
DB_USER=CHANGE_ME
DB_PASSWORD=CHANGE_ME
DB_HOST=CHANGE_ME
DB_PORT=CHANGE_ME
DB_DATABASE=CHANGE_ME
```

## Running locally

```bash
cd app
npm install
npm run dev
```

```bash
cd api
pip install pipenv
pipenv shell
pipenv install
python run.py
```

### Using Docker

```bash
docker compose up
```

## References

- https://youtu.be/D1W8H4Rkb9A?si=fj1uA7W2Ri5rAoCa
- https://github.com/FaztWeb/flask-react-mongodb-crud
