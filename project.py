from flask import *

app = Flask(__name__)


@app.route("/")
def render1():
    return render_template("render1.html");


@app.route("/Next")
def render2():
    return render_template("render2.html")


@app.route("/details", methods=["POST", "GET"])
def render3():
    msg = "msg"
    if request.method == "POST":
        return render_template("render3.html", msg=msg)


@app.route("/final")
def render4():
    return render_template("render4.html")


@app.route("/exit")
def renderlast():
    return render_template("render_last.html")


if __name__ == "__main__":
    app.run(port=3260)
