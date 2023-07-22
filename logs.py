from MlProject.logger import logging
from flask import Flask

app = Flask(__name__)

@app.route('/' , methods = ['GET', 'POST'])
def index():
    logging.info('Testing Is Logging Working as excpected')
    return "Logging is working as expected"

if __name__ == '__main__':
    app.run(debug=True)
