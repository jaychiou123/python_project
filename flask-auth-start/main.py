from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fa8f1bf0378cada66d5655325c826674746310cec9b72940ff361f6e623d2c9d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        p_to_hash = generate_password_hash(request.form['password'], 'pbkdf2:sha256', salt_length=8)
        if User.query.filter_by(email=request.form['email']).first():
            flash("The email has already been signed up, try again.")
            return redirect(url_for('login'))
        else:
            new_user = User(email=request.form['email'], password=p_to_hash, name=request.form["name"])
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets", name=request.form["name"]))
    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user == None:
            flash("This email doesn't exist, please try again!")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("This password is wrong, please try again!")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for("secrets", name=user.name))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory('./static/files',
                               "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

