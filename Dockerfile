# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update -qq \
  && apt-get install -y curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY 'e5f11a4aa1422222cee96b2fbb876a455de6d376a5f74cf3'



# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt


# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Start server
CMD python manage.py migrate && python manage.py createsuperuser && gunicorn HLSBACK.wsgi:application --bind 0.0.0.0:8000