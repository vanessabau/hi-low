from flask import Flask, request, render_template_string
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Guess a number between 0 and 9</h1>
        <form action="/guess" method="post">
            <input type="number" name="guess" min="0" max="9" required style="width: 150px; margin-bottom: 25px;"/>
            <button type="submit" style="width: 150px; margin-bottom: 25px;">Submit Your Guess</button>
        </form>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>
    </body>
</html>
"""

@app.route('/')
def home():
    return home_page


@app.route("/guess", methods=["POST"])
def guess_number():
    guess = int(request.form["guess"])
    if guess > random_number:
        response = "<h1 style='color: purple'>Too high, try again!</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_number:
        response = "<h1 style='color: red'>Too low, try again!</h1>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        response = "<h1 style='color: green'>You found me!</h1>" \
                   "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

    reset_button = """
        <form action="/" method="get">
            <button type="submit" style="width: 150px; margin-top: 25px;">Try Again</button>
        </form>
    """
    return response + reset_button


if __name__ == "__main__":
    app.run(debug=True)