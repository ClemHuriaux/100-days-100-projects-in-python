from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rand

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
SECRET_API_KEY = "TopSecretAPIKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<{self.name}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = rand.choice(cafes)
    print(random_cafe)


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.as_dict() for cafe in cafes])


@app.route("/search")
def get_cafe_at_location():
    loc = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=loc).first()
    if cafe:
        return jsonify(cafe=cafe.as_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id_cafe>", methods=['PATCH'])
def update_price(id_cafe):
    new_price = request.args.get("new_price")
    cafe_to_update = Cafe.query.get(id_cafe)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Succesfuly updated the price")
    return jsonify(error={"Not Found": "There is no cafe with this id in the database"})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id_cafe>", methods=["DELETE"])
def delete_cafes(id_cafe):
    api_key = request.args.get("api-key")
    if api_key == SECRET_API_KEY:
        cafe_to_update = Cafe.query.get(id_cafe)
        if cafe_to_update:
            db.session.delete(cafe_to_update)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
