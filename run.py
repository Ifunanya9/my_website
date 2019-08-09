from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apple", "Pear", "Banana"]

    return render_template("index.html")

@app.route("/profile")
def name():
    paragraph = "<p>My name is Ifunanyachi</p>"
    return "My profile" + paragraph