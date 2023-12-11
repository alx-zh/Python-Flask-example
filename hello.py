from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/test')
def test():
    return render_template("index.html")


@app.route("/about")
def get_page_about():
    return render_template("about.html", 
                           h1 = "О приложении",
                           content = "Page contains information text")

""" 


@app.route("/")
def index():
    return render_template("index.html")






    def hello_world():
    return "<p>Hello, World!</p>"
"""

if __name__ == '__main__':
    app.run(debug=True)