# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Set ChromeDriver path in the container
COPY C:\Users\sanja\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe /usr/local/bin/

# Run the Python script when the container launches
CMD ["python", "app.py"]
