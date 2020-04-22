from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app =  Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.secret_key = "somesecret_key123"
api = Api(app)

@app.before_first_request
def create_dbstruc():
    db1.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")i
api.add_resource(ItemList, "/items")

api.add_resource(Store, "/stores/<string:name>")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    from db import db1
    db1.init_app(app)
    app.run(debug=True)