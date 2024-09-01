from flask import redirect, render_template, Flask, request
from werkzeug import Response
app = Flask(__name__)

log:str = ""

@app.route('/')
def index() -> str:
    return render_template('index.html',log=log)

@app.route("/input",methods=["POST"])
def input() -> Response:
    global log
    log = request.form["log"]
    return redirect("/")
