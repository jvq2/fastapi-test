# Normally I would want to use a less pre-configured image to have more control/customization.
# This image was chosen for expedience/simplicity
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app

RUN pip install -r /app/requirements.txt
