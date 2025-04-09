import flask
app = flask.Flask(__name__)
@app.route('/index')
def index():
    return flask.render_template('index.html')
@app.route('/conf')
def conf():
    return flask.render_template('conf.html')
app.run(port='3000')