from flask import render_template, Blueprint

# create a Blueprint instance
bp = Blueprint("index", __name__)

# Define your view functions within the Blueprint
@bp.route("/")
def index():
    return render_template("index.html")