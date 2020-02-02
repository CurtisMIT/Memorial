from app import db

class Person(db.Model):
    __tablename__ = 'people'

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String())
    birth   = db.Column(db.String())
    dead    = db.Column(db.String())
    bio     = db.Column(db.String())
    milestones = db.relationship('Milestone', backref='Person')
    entries = db.relationship('Entry', backref='Person')

    def __init__(self, name, birth, dead, bio):
        self.name = name
        self.birth = birth 
        self.dead = dead 
        self.bio = bio

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth': self.birth,
            'dead': self.dead,
            'bio': self.bio
        }

class Milestone(db.Model):
    __tablename__ = 'milestones'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    year = db.Column(db.String())
    description = db.Column(db.String())
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __init__(self, title, year, description, person_id):
        self.title = title
        self.year = year 
        self.description = description
        self.person_id = person_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'description': self.description,
            'person_id': self.person_id
        }

class Entry(db.Model):
    __tablename__ = 'guest_entries'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __init__(self, content, person_id):
        self.content = content 
        self.person_id = person_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'person_id': self.person_id
        }