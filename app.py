from random import randint

from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", "GET"])
def _start():
    if request.method == "GET":
        return render_template("start_form.html")
    if request.method == "POST":
        return render_template("form.html", min_=0, max_=1000, guess_num=500)


@app.route("/game", methods=["POST", "GET"])
def main():
    if request.method == "POST":

        min_num = request.form.get("min_")
        max_num = request.form.get("max_")
        min_num = float(min_num)
        max_num = float(max_num)

        guess = request.form.get("guess_num")
        guess = float(guess)

        if request.form["answer"] == "Too small":
            min_num = guess
        elif request.form["answer"] == "Too big":
            max_num = guess
        elif request.form["answer"] == "You win":
            guess = str(guess)
            return render_template("win.html", guess_num=str(guess[:-2]))

        guess = int((max_num - min_num)) / 2 + min_num
        guess = str(guess)
        return render_template("form.html",
                               min_=str(min_num),
                               max_=str(max_num),
                               guess_num=guess[:-2])

    if request.method == "GET":
        return render_template("form.html", min_=0, max_=1000, guess_num=500)


if __name__ == "__main__":
    app.run(debug=True)
