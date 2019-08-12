from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apple", "Pear", "Banana"]

    return render_template("start.html", name="Ifunanyachi Kanu", items=items)

@app.route("/profile")
def name():
    paragraph = "<h4>My name is Ifunanyachi</h4>"
    return "<h1>My profile</h1>" + paragraph