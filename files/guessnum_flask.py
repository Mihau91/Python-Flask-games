from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        min_value = 0
        max_value = 1000
        return render_template("welcome_page.html", min=min_value, max=max_value)
    else:
        return render_template("main_page.html")

if __name__ == '__main__':
    app.run(debug=True)
