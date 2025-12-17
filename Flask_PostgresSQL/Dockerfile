# Use an official Python runtime as a parent image
FROM python:3.13-alpine as builder

# Set the working directory in the container
WORKDIR /tmp/

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /tmp/

# Install any needed packages
RUN pip install pipenv
RUN pipenv install --system --deploy

# Use a multi-stage build to reduce the size of the final image
FROM python:3.13-alpine

# Set the working directory in the container to /flask-app
WORKDIR /flask-app

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Create a non-root user to run the application
RUN adduser -D flaskuser
USER flaskuser

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run run.py when the container launches
CMD ["python", "run.py", "--host=0.0.0.0"]
