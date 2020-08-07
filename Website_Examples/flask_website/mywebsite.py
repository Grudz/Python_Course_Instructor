# Website by Ben Grudzien, refer to techwithtim

from flask import Flask, redirect, url_for, render_template, request, session, flash # Allows for redirects, render function allows for external html
# Request determines GET or POST

from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Creating flask instance
app.secret_key = "password" # could be any string lol, good to be complex (needed for session)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # User is table name
app.config["SQLALCHEMY_TRACK_MODIFCICATIONS"] = False # gets rid of errors
app.permanent_session_lifetime = timedelta(minutes=5) # Store log in session data from 5 days/mins

db = SQLAlchemy(app)

# Avoid quereies and writing this in python
class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100)) # Adding string column to database called email

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/") # type / to go to webpage
def home():
    return render_template("index.html") # How to render html templates (python = backend, html = frontend)

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())
    

@app.route("/login", methods = ["POST", "GET"]) # Normal method is GET
def login():
    if request.method == "POST":
        session.permanent = True # refer to above, false should make it go away after browser closes
        user = request.form["nm"] # nm is dictionary key from html file
        session["user"] = user

        found_user = users.query.filter_by(name=user).first() # first b/c 1 user with 1 name. all()
        #found_user = users.query.filter_by(name=user).delete() - How to delete an object
        #for user in found_user:
           #user.delete()
        if found_user:
            session["email"] = found_user.email            
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit() # adds to database (waiting to be finally saved)
        
        flash("Login Successful")
        return redirect(url_for("user")) # (url_for("user", usr = user)) < this needed without session
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
            
        return render_template("user.html", email=email)
    else:
        flash("Not Logged In!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info") # catagory, warning and error too (these are icons)
    session.pop("user", None)
    session.pop("email", None) # Remove email when loser logs out
    return redirect(url_for("login"))

if __name__ == "__main__": # Starting website
    db.create_all()
    app.run() # Automatically updates website if pass debug = True

''' 5
app = Flask(__name__) # Creating flask instance
app.secret_key = "password" # could be any string lol, good to be complex (needed for session)
app.permanent_session_lifetime = timedelta(minutes=5) # Store log in session data from 5 days/mins

@app.route("/") # type / to go to webpage
def home():
    return render_template("index.html") # How to render html templates (python = backend, html = frontend)

@app.route("/login", methods = ["POST", "GET"]) # Normal method is GET
def login():
    if request.method == "POST":
        session.permanent = True # refer to above, false should make it go away after browser closes
        user = request.form["nm"] # nm is dictionary key from html file
        session["user"] = user
        flash("Login Successful")
        return redirect(url_for("user")) # (url_for("user", usr = user)) < this needed without session
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Not Logged In!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info") # catagory, warning and error too (these are icons)
    session.pop("user", None)
    return redirect(url_for("login"))

#Made this change during vid - created session so not /ben or whatever
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__": # Starting website
    app.run() # Automatically updates website if pass debug = True
'''
''' 4
app = Flask(__name__) # Creating flask instance

@app.route("/") # type / to go to webpage
def home():
    return render_template("index.html") # How to render html templates (python = backend, html = frontend)

@app.route("/test") # type / to go to webpage
def test():
    return render_template("new.html")

if __name__ == "__main__": # Starting website
    app.run() # Automatically updates website if pass debug = True
'''

''' 3
@app.route("/<name>") # type / to go to webpage
def home(name):
    return render_template("index.html", content = "Testing") # How to render html templates (python = backend, html = frontend)

if __name__ == "__main__": # Starting website
    app.run() # Automatically updates website if pass debug = True
'''

''' 2

@app.route("/<name>") # type / to go to webpage
def home(name):
    return render_template("index.html", content = ["Logan", "Sami", "Aly"]) # How to render html templates (python = backend, html = frontend)



if __name__ == "__main__": # Starting website
    app.run()
'''

''' 1
@app.route("/") # type / to go to webpage
def home():
    return "Hello, this is main page <h1>HELLO</h1>" # Can add inline html

@app.route("/<name>") # will display whatever name is typed in searchbar
def user(name):
    return f"Hello {name}!" # Works do url/ben or url/home to see it work

@app.route("/admin/") # creates redirect (type /admin and watch redirect to home), could use 1 or 2 slashes
def admin():
    return redirect(url_for("user", name="Admin!")) # string is name of function
'''
