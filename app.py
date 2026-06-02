from flask import Flask, render_template, redirect, request
import sqlite3
import random

app = Flask(__name__)


# Создание базы данных
def get_db():
    conn = sqlite3.connect("database.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER,
        url TEXT
    )
    """)

    conn.commit()
    conn.close()


# создаём БД при старте
get_db()


# главная страница
@app.route("/")
@app.route("/home")
def main():
    return render_template("index.html")


# создание короткой ссылки
@app.route("/shorten", methods=["POST"])
def submit():

    url_one = request.form["original_url"]

    # генерируем хеш
    hesh = random.randint(10000000, 99999999)

    # сохраняем в БД
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


# переход по короткой ссылке
@app.route("/<hesh>")
def reload(hesh):

    conn = sqlite3.connect("database.db")

    url = conn.execute(
        "SELECT url FROM users WHERE id = ?",
        (hesh,)
    ).fetchone()

    conn.close()

    if url:
        return redirect(url[0])

    return "Ссылка не найдена", 404


if __name__ == "__main__":
    app.run(debug=True)