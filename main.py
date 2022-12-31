from flask import Flask, render_template, request, redirect, url_for
import sqlite3

db = sqlite3.connect("games-collection.db")
cursor = db.cursor()
app = Flask(__name__)

all_games = []


@app.route('/')
def home():
    return render_template('index.html', games=all_games)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_game = {
            "title": request.form["title"],
            "console": request.form["console"],
            "rating": request.form["rating"]
        }
        all_games.append(new_game)
        
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)


cursor.execute("CREATE TABLE games (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")