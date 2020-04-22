from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username Error.")
    parser.add_argument("password", type=str, required=True, help="Password Error.")

    def post(self):
        data = self.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message" : "User already exist in the repository"}, 400

        item = UserModel(**data)
        item.save_to_db()

        return {"message" : "User created successfully."}, 201


