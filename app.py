from flask import Flask, request, jsonify, render_template, send_file, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["IMAGE_UPLOADS"] = "/Users/elaine/Desktop/projects/Memorial/templates"
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])

from models import Person, Milestone, Entry

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/add", methods = ['GET', 'POST'])
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
    
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

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

        f = request.files['file']
        f.save(secure_filename(f.filename))
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

@app.route("/milestone", methods = ['POST'])
def add_a_milestone():
    req_data = request.get_json()

    start = req_data['start']
    end = req_data['end']
    description = req_data['description']
    person_id = req_data['person_id']

    try:
        milestone = Milestone(
            start = start,
            end = end,
            description = description,
            person_id = person_id
        )
        db.session.add(milestone)
        db.session.commit()
        return "Milestone added. Milestone id = {}".format(milestone.id)
    except Exception as e:
        return(str(e))

# @app.route("/milestone/<person_id>")
# def getMilestone_by_id(person_id):
#     try:
#         person=Person.query.filter_by(person_id=person_id).first()
#         return jsonify(person.serialize())
#     except Exception as e:
# 	    return(str(e))

@app.route("/milestone/<id>", methods = ["GET"])
def get_milestones_from_id(id):
    try:
        milestone = Milestone.query.filter_by(person_id=id).first()
        return jsonify(milestone.serialize())
    except Exception as e:
        return(str(e))

@app.route("/entry", methods = ["POST"])
def add_an_entry():
    req_data = request.get_json()

    name = req_data['name']
    relation = req_data['relation']
    title = req_data['title']
    content = req_data['content']
    person_id = req_data['person_id']
    try:
        entry = Entry(
            name = name,
            relation = relation,
            title = title,
            content = content,
            person_id = person_id
        )
        db.session.add(entry)
        db.session.commit()
        return "Entry added. Entry id = {}".format(entry.id)
    except Exception as e:
        return(str(e))

@app.route("/entry/<id>", methods = ["GET"])
def get_entries_from_id(id):
    try:
        entry = Entry.query.filter_by(person_id=id).first()
        return jsonify(entry.serialize())
    except Exception as e:
        return(str(e))

    
if __name__ == '__main__':
    app.run()