from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=6, max=120)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data =="admin@email.com" and form.password.data == "12345678":
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)