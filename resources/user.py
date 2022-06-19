import email
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str,)
argumentos.add_argument('email', type=str)
argumentos.add_argument('telefone', type=int)
argumentos.add_argument('senha', type=str, required=True, help="This field 'senha' cannot be left blank")

class Users(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

class User(Resource):   
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    # def post(self, id):
    #     if UserModel.find_user(id):
    #         return {"message": "User id '{}' already exists.".format(id)}, 400

    #     dados = argumentos.parse_args()
    #     user = UserModel(id, **dados)
    #     try:
    #         user.save_user()
    #     except:
    #         return {'message': 'An internal error ocurred trying to save hotel.'}, 500
    #     return user.json()

    def put(self, id):
        dados = argumentos.parse_args()
        user_encontrado = UserModel.find_user(id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            user_encontrado.save_user()
            return user_encontrado.json(), 200 #OK
        user = UserModel(id, **dados)
        try:
            user.save_user()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return user.json(), 201 #created

class UserPost(Resource):
    def post(self):
        dados = argumentos.parse_args()
        
        if UserModel.find_by_email(dados['email']):
            return {"message": "User email '{}' already exists.".format(dados['email'])}, 400

        user = UserModel(**dados)
        try:
            user.save_user()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return user.json()


class UserDelete(Resource):
    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = argumentos.parse_args()

        user = UserModel.find_by_email(dados['email'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.id)
            return {'acess_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect.'}, 401