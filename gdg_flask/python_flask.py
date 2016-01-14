from gdg_flask import app

@app.route('/')
def hello_world():
    return 'Hello World!'
