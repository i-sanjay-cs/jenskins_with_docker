# Use an official Python runtime as a parent image
FROM python:3.8-buster

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
RUN install Flask

copy ./app
# Expose the Flask application port
EXPOSE 5000

# Run the Flask application when the container launches
CMD ["python", "app.py"]
