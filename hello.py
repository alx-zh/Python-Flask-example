from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("nwfiles/templates/index.html")

@app.route("/about")
def get_page_about():
    return render_template("about.html", h1 = "О приложении")


""" 
    def hello_world():
    return "<p>Hello, World!</p>"
"""
