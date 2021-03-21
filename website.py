import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html')

@app.route('/music')
def music():
    return flask.render_template('music.html')

@app.route('/recognition')
def recognition():
    return flask.render_template('recognition.html')

@app.route('/service')
def service():
    return flask.render_template('service.html')

@app.route('/work')
def work():
    return flask.render_template('work.html')

@app.route('/birding')
def birding():
    return flask.render_template('birding.html')

@app.route('/cv')
def cv():
    return flask.render_template('cv.html')

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
