# Tims referral for more advanced stuff: http://exploreflask.com/en/latest/blueprints.html
# just add admin folder with __init__.py and do from from admin.second (can use interior template/static folders)
# Tims vid: https://www.youtube.com/watch?v=WteIH6J9v64

from flask import Flask, render_template
from second import second # from py file import variable

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin") # the rest of url is passed to second.py

@app.route("/") # Renders second first even if same name
def test():
	return "<h1>Test</h1>"

if __name__ == "__main__":
	app.run(debug=True)

'''
@app.route("/home") # home page can be accessed with either / or /home
@app.route("/")
def home():
	return render_template("home.html")
	'''