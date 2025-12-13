from . import db

class Task(db.Model): # Inheriting from db.Model
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Task({self.id}, {self.content})"
    
    def __str__(self):
        return f"Task ID: {self.id} - Content: {self.content}"
