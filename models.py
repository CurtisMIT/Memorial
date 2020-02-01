from app import db

class Person(db.Model):
    __tablename__ = 'people'

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String())
    birth   = db.Column(db.String())
    dead    = db.Column(db.String())

    def __init__(self, name, birth, dead):
        self.name = name
        self.birth = birth 
        self.dead = dead 

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth': self.birth,
            'dead': self.dead
        }