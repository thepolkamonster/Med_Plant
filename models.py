from db import db

class LeafModel(db.Model):
    __tablename__ = "Leaves"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))

    def __init__ (self, name):
        self.name = name

    def __repr__(self):
        return f" ID: {self.id} -- NAME: {self.name}\n"