from . import db

class User(db.Model): # Inheriting from db.Model
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    registration = db.Column(db.DateTime(timezone=True), nullable=False, default=db.func.timezone('UTC', db.func.current_timestamp()))
    modification = db.Column(db.DateTime(timezone=True), onupdate=db.func.timezone('UTC', db.func.current_timestamp()))

    def __init__(self, fullname, email, password):
        self.fullname = fullname
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User({self.id}, {self.fullname}, {self.email}, {self.password[:10]}, \
            {self.registration}, {self.modification})"
    
    def __str__(self):
        return f"User ID: {self.id} - Name: {self.fullname} - Email: {self.email} - Password: {self.password[:10]} \
            - Registered On: {self.registration} - Last Modified: {self.modification}"

    def validate_email(self):
        if not self.email:
            raise ValueError("Email is required!")
        if "@" not in self.email:
            raise ValueError("Invalid email format!")
        
    def validate_password(self):
        if not self.password:
            raise ValueError("Password is required!")
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long!")

    def validate(self):
        self.validate_email()
        self.validate_password()
