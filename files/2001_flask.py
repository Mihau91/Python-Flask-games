from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template("main_2001.html")
    else:
        return redirect('/game')


@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("game_2001.html")


if __name__ == '__main__':
    app.run(debug=True)
