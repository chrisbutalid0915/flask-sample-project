from flask import render_template, Blueprint

# create a Blueprint instance
views = Blueprint("views", __name__)

# Define your view functions within the Blueprint
@views.route("/")
def index():
    return render_template("index.html")