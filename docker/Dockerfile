# pull the official base image
FROM python:3.8.1-slim-buster

    
#Adds user that will be used in the container
RUN useradd app_user

# Upgrade PIP
RUN python3 -m pip install --upgrade pip

# set work directory
WORKDIR /app


# Install the project requirements.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PORT=8000



# install all the dependencies/libraries indicated in the 'requirements.txt'
# COPY ../../requirements.txt .
# RUN pip install --no-cache-dir -r ./requirements.txt

# this path is relative depending on where the build was made from. e.g if docker
# calls this from the BASE DIR (where manage.py is), then all the paths must be
# relative to that position.
COPY . /app



# # Install the application server.
# RUN pip install "gunicorn==20.0.4"



# Expose port 8000 of the container, so it can 'connect' with the port of the host
EXPOSE 8000

# Execute $ python3 manage.py runserver "0.0.0.0:8000"
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
