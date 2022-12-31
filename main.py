from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_games = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_game = {
            "title": request.form["title"],
            "console": request.form["console"],
            "rating": request.form["rating"]
        }
        all_games.append(new_game)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

