FROM python:3.8

WORKDIR /app

# Move files to correct locations
COPY model/requirements.txt /app/model_requirements.txt
COPY test/requirements.txt /app/test_requirements.txt

# Install user requirements and test requirements
RUN pip install -r model_requirements.txt
RUN pip install -r test_requirements.txt

# Move test file to the project
COPY test/test.py /app/test.py
