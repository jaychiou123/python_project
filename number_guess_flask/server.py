from flask import Flask
import random

app = Flask(__name__)
n = random.randint(0, 9)
@app.route('/')
def hello_world():
    return '<h1> Guess a number between 0 and 9<h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def check(guess):
    if guess > n:
        return '<h1 style= "color:red"> Too high. Try again!<h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < n:
        return '<h1 style= "color:purple"> Too low. Try again!<h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style= "color:green"> You found me!!<h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
if __name__=="__main__":
    app.run(debug=True)