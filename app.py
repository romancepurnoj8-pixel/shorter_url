from flask import Flask, render_template, redirect, request
import sqlite3
import random 

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("database.db")
    conn.execute(""" CREATE TABLE IF NOT EXISTS users 
    ( 
    id INTEGER,
    url TEXT
    )
    """)
    conn.commit()

get_db()


@app.route("/")
@app.route("/home")
def main():
    return render_template("index.html")

import random

@app.route("/shorten", methods=["POST"])
def submit():
    url_one = request.form["original_url"]

    hesh = random.randint(10000000, 99999999)

    conn = sqlite3.connect("database.db")
    conn.execute(
        "INSERT INTO users (id, url) VALUES (?, ?)",
        (hesh, url_one)
    )
    conn.commit()
    conn.close()

    short_url = f"http://127.0.0.1:5000/{hesh}"

    return render_template(
        "index.html",
        user_input=url_one,
        short_url=short_url
    )


@app.route("/<hesh>")
def reload(hesh):
    url = cursor.execute(
            "SELECT url FROM users WHERE id = ?",
            (hesh,)
            ).fetchone()

    if url:
        return redirect(url[0])
   
if __name__ == "__main__":
    app.run()
