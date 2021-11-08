import app


@app.app.route('/')
@app.app.route('/index')
def index():
    return "Hello world!"
