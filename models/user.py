from db import db1

class UserModel(db1.Model):
    __tablename__ = "users"

    id = db1.Column(db1.Integer, primary_key=True)
    username = db1.Column(db1.String(80))
    password = db1.Column(db1.String(80))


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db1.session.add(self)
        db1.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
