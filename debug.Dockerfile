FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

# Move files to correct locations
COPY model/requirements.txt /app/model_requirements.txt
COPY debug/requirements.txt /app/debug_requirements.txt

# Install user requirements and test requirements
RUN pip install -r model_requirements.txt
RUN pip install -r debug_requirements.txt