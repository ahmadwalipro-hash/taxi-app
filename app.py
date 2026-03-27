from flask import Flask, render_template
from flask_cors import CORS
from auth import auth
from routes import routes
from models import create_tables

app = Flask(__name__)
app.secret_key = "secret123"
CORS(app)

# create database tables
create_tables()

# register blueprints
app.register_blueprint(auth)
app.register_blueprint(routes)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login_page")
def login_page():
    return render_template("login.html")

@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/driver")
def driver():
    return render_template("driver.html")

if __name__ == "__main__":
    app.run(debug=True)