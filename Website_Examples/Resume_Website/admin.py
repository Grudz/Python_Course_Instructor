from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates") # normally always __name__

@admin.route("/home")
@admin.route("/")
def home():
	return render_template("home.html")

@admin.route("/test")
def test():
	return "<h1>Test</h1>"


