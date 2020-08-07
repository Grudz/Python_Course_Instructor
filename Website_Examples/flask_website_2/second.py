from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates") # normally always __name__

@second.route("/home")
@second.route("/")
def home():
	return render_template("home.html")

@second.route("/test")
def test():
	return "<h1>Test</h1>"


