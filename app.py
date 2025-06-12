from flask import Flask, render_template
from contests_scr import get_all_data
import json
import os
from datetime import datetime

app = Flask(__name__)



def get_latest_data():
    today_str = datetime.now().strftime("%Y-%m-%d")
    file_name = f"data_{today_str}.json"
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    else:
        return None


@app.route("/")
def home():
    data = get_all_data()

    return render_template("index.html", data=data)

@app.route("/")
def datawtime():
    data = get_all_data()  
    latest_data = get_latest_data()  
    today_str = datetime.now().strftime("%Y-%m-%d")  


    if latest_data:
        date = today_str
    else:
        date = "Veri bulunamadı"

    return render_template("index.html", data=data, date=date)



@app.route("/archive/<date>")
def data_view(date):
    file_name = f"data_{date}.json"
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        return render_template("data_view.html", data=data)
    else:
        return f"{file_name} bulunamadı.", 404


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/archive")
def archive():
    files = [f for f in os.listdir() if f.startswith("data_") and f.endswith(".json")]
    files.sort(reverse=True)  # en yeni en üstte görünsün
    return render_template("archive.html", files=files)


if __name__ == "__main__":
    app.run(debug=True, port=5001)


