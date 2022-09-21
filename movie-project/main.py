from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

tmdb_key = "e3197b0f0a21207c7a1df4ad9e287c30"
tmdb_search_url = "https://api.themoviedb.org/3/search/movie"
tmdb_detail_url = "https://api.themoviedb.org/3/movie"
pic_url = "https://image.tmdb.org/t/p/original"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(400), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'

db.create_all()

class Editform(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class Addform(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Done')

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    movie_obj = db.session.query(Movie).order_by("rating").all()
    for i in range(len(movie_obj)):
        movie_obj[i].ranking = len(movie_obj) - i
    return render_template("index.html", obj=movie_obj)

@app.route("/edit", methods=["POST", "GET"])
def edit():
    form=Editform()
    movie_id = request.args.get("id")
    print(movie_id)
    movie_obj = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_obj.rating = float(form.rating.data)
        movie_obj.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", obj=movie_obj, form=form)

@app.route("/delete", methods=["POST", "GET"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["POST", "GET"])
def add():
    form=Addform()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        parameters = {
            "api_key": tmdb_key,
            "language": "en-US",
            "query": movie_title
        }
        response = requests.get(tmdb_search_url, params=parameters)
        movie_list = response.json()["results"]
        return render_template("select.html", movie_list=movie_list)
    return render_template("add.html", form=form)

@app.route("/select", methods=["POST", "GET"])
def select():
    movie_id = request.args.get("id")
    parameters = {
        "api_key": tmdb_key,
        "language": "en-US",
    }
    response = requests.get(tmdb_detail_url + "/" + movie_id, params=parameters)
    movie_detail = response.json()
    new_movie = Movie(title=movie_detail["original_title"], year=movie_detail["release_date"].split("-")[0],
                      description=movie_detail["overview"], img_url=pic_url + movie_detail["poster_path"])
    db.session.add(new_movie)
    db.session.commit()
    print(movie_detail["original_title"])
    print(movie_detail["release_date"].split("-")[0])
    print(pic_url + movie_detail["poster_path"])
    print(movie_detail["overview"])
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
