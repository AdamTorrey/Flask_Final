from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run()