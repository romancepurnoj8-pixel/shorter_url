from flask import Flask, render_template, redirect, request
import sqlite3
import random 

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("database.db")
    db.execute(""" CREATE TABLE IF EXISTS users 
    id INTGER,
    url TEXT""")
    conn.commit()


def genHESH():
    hesh = random.randint(10_000_000, 99_999_999)
    return(hesh)


@app.route("/")
@app.route("/home")
def main():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def submit():
        url_one = request.form["original_url"]
        print(url_one)

        return render_template(
                "index.html", 
                user_input=url_one,
                links=[]
                 )


@app.route("/<hesh>")
def reload(hesh):
    url = cursor.execute("SELECT url from users WHERE id = ?", 
            (hesh)
            )

if __name__ == "__main__":
    app.run()
