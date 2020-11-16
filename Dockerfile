# Normally I would want to use a less pre-configured image to have more control/customization.
# This image was chosen for expedience/simplicity
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copy ovver the application for requirements installation and production app.
# When run through docker-compose, the app filesystem is mounted as a shared volume for active editing.
COPY ./ /app

RUN pip install -r /app/requirements.txt
RUN apt-get install git
