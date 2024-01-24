"""
This is a module that utilizes the Flask web framework to create a webpage that displays Hello HBNB! Whatever that means.
"""
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") with the option strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root URL.

    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route handler for the root URL.

    Returns:
        str: A simple greeting message.
    """
    return 'HBNB'

# Define a route for "/c/<text>" with the option strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Route handler for "/c/<text>".

    Args:
        text (str): The value of the text variable.

    Returns:
        str: Display "C " followed by the value of the text variable.
    """
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return f'C {text}'

# Define a route for "/python/<text>" with the option strict_slashes=False
@app.route('/python/<text>/', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """Route handler for "/python/<text>".

    Args:
        text (str, optional): The value of the text variable. Defaults to "is cool".

    Returns:
        str: Display "Python " followed by the value of the text variable.
    """
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return f'Python {text}'

# Run the Flask application if the script is executed
if __name__ == '__main__':
    # Start the application on 0.0.0.0 (all available network interfaces) and port 5000
    app.run(host='0.0.0.0', port=5000)