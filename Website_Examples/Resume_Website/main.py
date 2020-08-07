# Tims referral for more advanced stuff: http://exploreflask.com/en/latest/blueprints.html
# just add admin folder with __init__.py and do from from admin.second (can use interior template/static folders)
# Tims vid: https://www.youtube.com/watch?v=WteIH6J9v64

from flask import Flask, render_template
from admin import admin # from py file import variable

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin") # the rest of url is passed to admin.py

@app.route("/") # Renders admin first even if same name
def home():
	return render_template("home.html")

@app.route("/embedded")
def embedded():
	return render_template("embedded.html")

@app.route("/autonomous")
def autonomous():
	return render_template("autonomous.html")

@app.route("/python")
def pythonclass():
	return render_template("pythonclass.html")

if __name__ == "__main__":
	app.run(debug=True)
