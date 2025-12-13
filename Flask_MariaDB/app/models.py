from . import db

class Contact(db.Model): # Inheriting from db.Model
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Contact({self.id}, {self.fullname}, {self.email}, {self.phone})"
    
    def __str__(self):
        return f"Contact ID: {self.id} - Name: {self.fullname} - Email: {self.email} - Phone: {self.phone}"

    def validate_email(self):
        if not self.email:
            raise ValueError("Email is required!")
        if "@" not in self.email:
            raise ValueError("Invalid email format!")

    def validate_phone(self):
        if not self.phone:
            raise ValueError("Phone number is required!")
        if not self.phone.isdigit():
            raise ValueError("Phone number must contain only digits!")

    def validate(self):
        self.validate_email()
        self.validate_phone()
