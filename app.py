from flask import Flask, render_template, redirect,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!! New to Flask <h1>WEB DEVELOPMENT</h1>";

@app.route("/<name>")
def user(name):
    return f"Hello {name}!";

@app.route("/admin")
def admin():
    return redirect(url_for("home"));

@app.route("/jumbled")
def hello_world():
    return render_template("jumbledword.html"); 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)