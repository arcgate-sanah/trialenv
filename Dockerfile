# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=newproject.settings
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /newproject

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy the Django project files into the container
COPY . /newproject/

# Install project dependencies
COPY requirements.txt /newproject/
RUN pip cache purge

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django
# Activate the virtual environment (if applicable)
# RUN source env/bin/activate 

# Set the PYTHONPATH (if needed)
# ENV PYTHONPATH=/path/to/your/django/project   
# Collect static files
RUN python manage.py collectstatic --noinput 2>&1 | tee collectstatic.log

# Create database tables and apply migrations
RUN pip install python-decouple
RUN pip install -U drf-yasg
RUN pip install djangorestframework
RUN pip install djangorestframework-simplejwt
RUN pip install psycopg



# Create a superuser (you can remove this line for production)


# # Expose the port the application will run on
# EXPOSE 8000

# Start the application
RUN python manage.py collectstatic --noinput

RUN pip install gunicorn
CMD ["gunicorn", "newproject.wsgi:application", "--bind", "0.0.0.0:8000"]

