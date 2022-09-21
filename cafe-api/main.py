from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##No found dict
no_found={
    "Not Found": "Sorry, we don't have a cafe at that location."
}
##Successful add
add_succ={
    "success": "Successfully added the new cafe."
}
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

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/all")
def get_all_cafes():
    cafe_list = []
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        cafe_list.append(cafe.to_dict())
    print(cafe_list)
    return jsonify(cafes=cafe_list)

@app.route("/random", methods=["GET"])
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe_chosen = random.choice(all_cafes)
    return jsonify(cafes=cafe_chosen.to_dict())

@app.route("/search")
def research_cafe():
    local = request.args.get("loc")
    cafes_selected = Cafe.query.filter_by(location=local).first()
    if cafes_selected == None:
        return jsonify(error=no_found)
    else:
        return jsonify(cafes=cafes_selected.to_dict())

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response=add_succ)

@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update == None:
        return jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database."})
    else:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify({"success":"Successfully updated the price."})

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    key = request.args.get("api-key")
    if key != "TopSecretAPIKey":
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})
    elif cafe_to_delete == None:
        return jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database."})
    else:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify({"success": "Successfully deleted the cafe."})
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
