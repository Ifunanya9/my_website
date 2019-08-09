from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apple", "Pear", "Banana"]
    output = ""
    for item in items:
        output += "<h3>" + item + "</h3>"

    return output

@app.route("/profile")
def name():
    paragraph = "<p>My name is Ifunanyachi</p>"
    return "My profile" + paragraph