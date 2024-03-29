# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY app.py requirements.txt ./

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask application port
EXPOSE 5000

# Run the Flask application when the container launches
CMD ["python", "app.py", "&", "sleep", "300", "&&", "pkill", "python"]
