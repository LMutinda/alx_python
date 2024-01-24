
"""
This module uses the Flask web framework to create web applications
"""
from flask import Flask
 
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Method to display text on web page

    Args:
        None

    Returns:
        Text
    
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)s