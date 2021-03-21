import flask

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31557601 # 1 year 1 second, because prime

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

# Is there a cleaner way of handling these redirects?

@app.route('/index.html')
def index_old():
    return flask.redirect(flask.url_for('index'))

@app.route('/birding.html')
def birding_old():
    return flask.redirect(flask.url_for('birding'))

@app.route('/music.html')
def music_old():
    return flask.redirect(flask.url_for('music'))

@app.route('/cv.html')
def cv_old():
    return flask.redirect(flask.url_for('cv'))

@app.route('/service.html')
def service_old():
    return flask.redirect(flask.url_for('service'))

@app.route('/work.html')
def work_old():
    return flask.redirect(flask.url_for('work'))

@app.route('/recognition.html')
def recognition_old():
    return flask.redirect(flask.url_for('recognition'))

@app.route('/contact.html')
def contact_old():
    return flask.redirect(flask.url_for('contact'))

if __name__ == '__main__':
    app.run()
