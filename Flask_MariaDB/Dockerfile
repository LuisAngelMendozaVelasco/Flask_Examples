# Use an official Python runtime as a parent image
FROM python:3.13-slim as builder

# Set the working directory in the container
WORKDIR /tmp/

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /tmp/

# Install build dependencies and MariaDB Connector/C dev libs so Python
# packages that require the native connector can be built in this stage.
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	python3-dev \
	libmariadb-dev \
	libssl-dev \
	libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv
RUN pipenv install --system --deploy

# Use a multi-stage build to reduce the size of the final image
FROM python:3.13-slim

# Set the working directory in the container to /flask-app
WORKDIR /flask-app

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Install runtime libraries for MariaDB Connector/C so compiled Python
# extensions can link at runtime.
RUN apt-get update && apt-get install -y --no-install-recommends \
	libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user to run the application
RUN adduser flaskuser
USER flaskuser

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run run.py when the container launches
CMD ["python", "run.py", "--host=0.0.0.0"]
