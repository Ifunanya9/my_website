from flask import Flask, render_template, request
app = Flask(__name__)

class Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
@app.route("/")
def hello():

    # items = [
    #     Item("Apple", 5),
    #     Item("Pear", 7),
    #     Item("Banana", 8),
    #     Item("Computer", 1)
    # ]
    items = [
        {"name": "Apple", "amount": 5},
        {"name": "Pear", "amount": 7},
        {"name": "Banana", "amount": 8},
        {"name": "Computer", "amount": 1}
    ]

    for item in items:
        item["amount"] = item["amount"] * 2


    person = ("John", "Doe")

    output = render_template("start.html", person=person, items=items)
    return output

@app.route("/profile")
def name():
    return render_template("index.html")

@app.route("/test")
def test():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("test.html", name=name, age=age)
