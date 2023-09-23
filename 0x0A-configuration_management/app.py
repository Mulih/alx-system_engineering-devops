from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the Flask application
if __name__ == '__main__':
    app.run()
