from flask import Flask, render_template
from contests_scr import get_all_data

app = Flask(__name__)


@app.route("/")
def home():
    data = get_all_data()

    return render_template("index.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)


