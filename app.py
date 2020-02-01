from flask import Flask, request, jsonify, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/database_files/filestorage.db'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])

from models import Person

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/add")
def add_person():
    name    =request.args.get('name')
    birth   =request.args.get('birth')
    dead    =request.args.get('dead')
    bio     =request.args.get('bio')
    try:
        person=Person(
            name    =name,
            birth   =birth,
            dead    =dead,
            bio     =bio,
        )
        db.session.add(person)
        db.session.commit()
        return "person added. person id={}".format(person.id)
    except Exception as e:
	    return(str(e))
#http://127.0.0.1:5000/add?name=Twilight&birth=Stephenie Meyer&dead=2006

#returns a list of all deceased 
@app.route("/getall")
def get_all():
    try:
        people=Person.query.all()
        return jsonify([e.serialize() for e in people])
    except Exception as e:
	    return(str(e))

#returns the deceased info based on given id 
@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        person=Person.query.filter_by(id=id_).first()
        return jsonify(person.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/add/form", methods=['GET', 'POST'])
def add_person_form():
    if request.method == 'POST':
        name    =request.form.get('name')
        birth   =request.form.get('birth')
        dead    =request.form.get('dead')
        bio     =request.form.get('bio')
        try:
            person=Person(
                name    =name,
                birth   =birth,
                dead    =dead,
                bio     =bio,
            )
            db.session.add(person)
            db.session.commit()
            return "Person added. person id={}".format(person.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")
    
if __name__ == '__main__':
    app.run()