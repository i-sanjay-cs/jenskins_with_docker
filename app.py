from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
    
    # Delay execution for 5 seconds
    time.sleep(5)
    # After 5 seconds, stop the Flask app
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
