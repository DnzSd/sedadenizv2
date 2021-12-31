import os
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("main.html")

@app.route("/mission")
def mission_page():
    return render_template("mission.html")

@app.route("/sukaplumbagasi")
def mission2_page():
    return render_template("mission2.html")

@app.route("/534")
def mission3_page():
    return render_template("mission3.html")

@app.route("/306metre")
def mission4_page():
    return render_template("mission4.html")

@app.route("/eu4")
def mission5_page():
    return render_template("mission5.html")

@app.route("/ulyssesmoore")
def mission6_page():
    return render_template("mission6.html")

@app.route("/mackaandirin")
def mission7_page():
    return render_template("mission7.html")

@app.route("/cordoba")
def mission8_page():
    return render_template("mission8.html")

@app.route("/370kg")
def mission9_page():
    return render_template("mission9.html")

@app.route("/forrestgump")
def mission10_page():
    return render_template("mission10.html")

@app.route("/sedapiyadeoglu")
def final_page():
    return render_template("final.html")

@app.route("/foodgallery")
def food_gallery_page():
    return render_template("foodgallery.html")


if __name__ == "__main__":
    app.run()
