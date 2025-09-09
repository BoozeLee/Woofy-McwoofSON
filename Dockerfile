# 🐾 WOOFY McWOOFSON Dockerfile for Google Cloud Run
# This Dockerfile is configured for a Python Flask application.

# Use an official lightweight Python image
# Use a version consistent with your CI and project requirements.
FROM python:3.11-slim

# Set environment variables to ensure logs are sent straight to Cloud Run
ENV PYTHONUNBUFFERED True

# Set the working directory in the container
ENV APP_HOME /app
WORKDIR /app

# Copy local code to the container
COPY . ./

# Install production dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup using a production-grade server (gunicorn).
# Cloud Run automatically provides the $PORT environment variable.
# Point to the Flask app instance in your server file.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 cloudy_mccodeface.web.server:app