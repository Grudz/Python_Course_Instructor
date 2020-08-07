from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # Creating a flask instance

@app.route("/") # home webpage
def home():
    return "Hello, this main page. <h1>BEN</h1>" # inline HTML
'''
@app.route("/<name>") # Will display name variable
def user(name):
    return f"Hello {name}!" # Called on f string
'''

@app.route("/<name>") # Will display name variable
def user(name):
    return render_template("index.html", content = ["Ben", "Sami", "Aly"])

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__": # starting website
    app.run()



