From python:3.8-slim
RUN pip install --no-cache-dir -r requirements.txt
COPY chromedriver.exe /usr/local/bin/
CMD ["python", "app.py"]

