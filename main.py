"""`main` is the top level module for your Flask application."""
# Note: You don't need to call app.run() when running `dev_appserver.py .` or deploying to App Engine,
# since the application is embedded within the App Engine WSGI application server.

import sys
from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")

if __name__ == "__main__":
	container = sys.argv[1]
	print(container)

	if container == 'y':
		# running inside of a container
		print('Running inside of container')
		app.run(host='0.0.0.0', debug=True)
	else:
		app.run(debug=True)
    
