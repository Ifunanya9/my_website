from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apple", "Pear", "Banana"]
    output = render_template("start.html", name="Ifunanyachi Kanu", items=items)
    print(output)
    return output



@app.route("/profile")
def name():
    paragraph = "<h4>My name is Ifunanyachi</h4>"
    return "<h1>My profile</h1>" + paragraph

@app.route("/test")
def test():
    print(request)
    return render_template("test.html", name="Ifunanyachi Kanu")