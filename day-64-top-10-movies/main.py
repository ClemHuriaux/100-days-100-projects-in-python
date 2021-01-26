from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from sqlalchemy.exc import SQLAlchemyError
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

URL_MOVIE_API = "https://api.themoviedb.org/3"
MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
# try:
#     db.session.add(new_movie)
#     db.session.commit()
# except SQLAlchemyError:
#     pass


class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5")
    review = StringField(label="Your review")
    submit = SubmitField(label="Submit")


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title")
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()
    new_url = f"{URL_MOVIE_API}/search/movie"
    if form.validate_on_submit():
        parameters = {
            "api_key": MOVIE_API_KEY,
            "query": form.title.data
        }
        response = requests.get(new_url, params=parameters)
        response.raise_for_status()
        return render_template("select.html", options=response.json()["results"])
    return render_template("add.html", form=form)


@app.route("/find_movie")
def find_movie():
    movie_id = request.args.get("id")
    new_url = f"{URL_MOVIE_API}/movie/{movie_id}"
    response = requests.get(new_url, params={"api_key": MOVIE_API_KEY})
    response.raise_for_status()
    data = response.json()
    new_movie_to_add = Movie(
        title=data["title"],
        year=data["release_date"][:4],
        description=data["overview"],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
    )
    try:
        db.session.add(new_movie_to_add)
        db.session.commit()
    except SQLAlchemyError:
        pass
    return redirect(url_for("edit", id=new_movie_to_add.id))


if __name__ == '__main__':
    app.run(debug=True)
