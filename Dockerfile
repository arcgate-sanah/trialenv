# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=projectname.settings

# Create and set the working directory
WORKDIR /newproject/


# Expose port 8000 for the Django development server
EXPOSE 8000


