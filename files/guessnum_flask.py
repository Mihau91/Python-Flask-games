from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """
    Main function to render html files and handling game's logic.
    """
    if request.method == "GET":
        min_value = 0
        max_value = 1000
        return render_template("welcome_page.html", min=min_value, max=max_value)
    else:
        min_number = int(request.form.get("min"))  # takes values from html
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you win!":
            return render_template("win_page.html", guess=guess)  # if true render win_page.html

        guess = (max_number - min_number) // 2 + min_number  # calculations to get guess number

        return render_template("main_page.html", guess=guess, min=min_number, max=max_number)  # render main page


if __name__ == '__main__':
    app.run(debug=True)
