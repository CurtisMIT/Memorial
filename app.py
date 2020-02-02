from flask import Flask, request, jsonify, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/database_files/filestorage.db'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])

from models import Person, Milestone, Entry

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

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

#returns a list of all deceased 
@app.route("/getall")
def get_all():
    try:
        people=Person.query.all()
        return jsonify([e.serialize() for e in people])
    except Exception as e:
	    return(str(e))

#returns the deceased info based on given id 
@app.route("/person/<id>")
def get_by_id(id):
    try:
        person=Person.query.filter_by(id=id).first()
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

@app.route("/person", methods=["POST"])
def create_a_person():
    req_data = request.get_json()

    name = req_data['name']
    birth = req_data['birth']
    dead = req_data['dead']
    bio = req_data['bio']

    try:
        person = Person(
            name = name,
            birth = birth,
            dead = dead,
            bio = bio
        )
        db.session.add(person)
        db.session.commit()
        return "Person added. Person id = {}".format(person.id)
    except Exception as e:
        return(str(e))

@app.route("/")


@app.route("/milestone", methods = ['POST'])
def add_a_milestone():
    req_data = request.get_json()

    title = req_data['title']
    year = req_data['year']
    description = req_data['description']
    person_id = req_data['person_id']

    try:
        milestone = Milestone(
            title = title,
            year = year,
            description = description,
            person_id = person_id
        )
        db.session.add(milestone)
        db.session.commit()
        return "Milestone added. Milestone id = {}".format(milestone.id)
    except Exception as e:
        return(str(e))

@app.route("/entry", methods = ["POST"])
def add_an_entry():
    req_data = request.get_json()

    content = req_data['content']
    person_id = req_data['person_id']
    try:
        entry = Entry(
            content = content,
            person_id = person_id
        )
        db.session.add(entry)
        db.session.commit()
        return "Entry added. Entry id = {}".format(entry.id)
    except Exception as e:
        return(str(e))
    
if __name__ == '__main__':
    app.run()