from . import mongo
from bson.objectid import ObjectId

class User:
    def __init__(self, fullname, email, password, registration=None, modification=None, _id=None):
        self._id = _id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.registration = registration
        self.modification = modification

    def save(self):
        user_data = {
            'fullname': self.fullname,
            'email': self.email,
            'password': self.password,
            'registration': self.registration,
            'modification': self.modification
        }
        if self._id:
            mongo.db.users.update_one({'_id': self._id}, {'$set': user_data})
        else:
            result = mongo.db.users.insert_one(user_data)
            self._id = result.inserted_id
    
    def delete(self):
        mongo.db.users.delete_one({'_id': self._id})

    @classmethod
    def find_by_id(cls, _id):
        user_data = mongo.db.users.find_one({'_id': ObjectId(_id)})
        if user_data:
            return cls(
                _id=user_data['_id'],
                fullname=user_data['fullname'],
                email=user_data['email'],
                password=user_data['password'],
                registration=user_data['registration'],
                modification=user_data['modification']
            )
        return None

    @classmethod
    def find_all(cls):
        users = mongo.db.users.find()
        return [cls(
            _id=user['_id'],
            fullname=user['fullname'],
            email=user['email'],
            password=user['password'],
            registration=user['registration'],
            modification=user['modification']
        ) for user in users]

    def __repr__(self):
        return f"User({self._id}, {self.fullname}, {self.email}, {self.password[:10]}, {self.registration}, {self.modification})"

    def __str__(self):
        return f"User ID: {self._id} - Name: {self.fullname} - Email: {self.email} - Password: {self.password[:10]} - Registered On: {self.registration} - Last Modified: {self.modification}"

    def validate_email(self):
        if not self.email:
            raise ValueError("Email is required!")
        if "@" not in self.email:
            raise ValueError("Invalid email format!")
        if " " in self.email:
            raise ValueError("Email should not contain spaces!")
        if "." not in self.email.split("@")[-1]:
            raise ValueError("Invalid email format!")
        
    def validate_password(self):
        if not self.password:
            raise ValueError("Password is required!")
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long!")
        if not any(char.isupper() for char in self.password):
            raise ValueError("Password must contain at least one uppercase letter!")
        if not any(char.islower() for char in self.password):
            raise ValueError("Password must contain at least one lowercase letter!")
        if not any(char.isdigit() for char in self.password):
            raise ValueError("Password must contain at least one digit!")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in self.password):
            raise ValueError("Password must contain at least one special character!")

    def validate(self):
        self.validate_email()
        self.validate_password()

    def to_dict(self):
        return {
            '_id': self._id,
            'fullname': self.fullname,
            'email': self.email,
            'password': self.password,
            'registration': self.registration,
            'modification': self.modification
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data.get('_id'),
            fullname=data['fullname'],
            email=data['email'],
            password=data['password'],
            registration=data.get('registration'),
            modification=data.get('modification')
        )
