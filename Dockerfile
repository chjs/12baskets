# Pull the base image
FROM python:3.13.3-slim

# Set the working directory
WORKDIR /app

# Set environment variables to avoid Python buffering and to ensure UTF-8 encoding
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

# Install system dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
