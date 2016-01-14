
from flask import Flask

app = Flask(__name__)

from gdg_flask import app


if __name__ == '__main__':
    app.run(port=5002)

