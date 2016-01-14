<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5002)
=======
from gdg_flask import app

if __name__ == '__main__':
    app.run(port=5003)
>>>>>>> eef704575e89b2cf8e1561e5718eb22046863a51
