from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/reservations')
def reservations():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from reservations")

    rows = cur.fetchall();
    return render_template("reserved.html", rows = rows)

@app.route('/reserveform')
def reserve_form():
    return render_template('reserve_form.html')

@app.route('/reserverecord', methods = ['post'])
def reserve_record():
    try:
        name = request.form['name']
        roomNum = request.form['roomNum']
        checkIn = request.form['checkIn']
        checkOut = request.form['checkOut']
        email = request.form['email']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            q = "INSERT INTO reservations (name, roomNum, checkIn, checkOut, email) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(name, roomNum, checkIn, checkOut, email)
            cur.execute(q)

            con.commit()
            msg = "Thank you '{0}' for choosing to stay with us. Your room '{1}' has successfully been reserved!".format(name, roomNum)

    except:
        con.rollback()
        msg = "We're sorry. Your reservation has not gone through. Please try again!"

    finally:
        return render_template("reserve_record.html", msg = msg)
        con.close

if __name__ == "__main__":
    app.run()