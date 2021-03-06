from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST
import traceback

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str)
argumentos.add_argument('email', type=str, required=True, help="This field 'email' cannot be left blank")
argumentos.add_argument('telefone', type=int)
argumentos.add_argument('senha', type=str, required=True, help="This field 'senha' cannot be left blank")
argumentos.add_argument('ativado', type=bool)

class Users(Resource):
    query_params = reqparse.RequestParser()
    query_params.add_argument("nome", type=str, default="", location="args")
    query_params.add_argument("email", type=str, default="", location="args")
    query_params.add_argument("telefone", type=int, default="", location="args")

    def get(self):
        filters = Users.query_params.parse_args()
 
        query = UserModel.query
 
        if filters["nome"]:
            query = query.filter(UserModel.nome == filters["nome"])
        if filters["email"]:
            query = query.filter(UserModel.email == filters["email"])
        if filters["telefone"]:
            query = query.filter(UserModel.telefone == filters["telefone"])
 
        return {"users": [user.json() for user in query]}
        
class User(Resource):   
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

class UserPut(Resource):

    @jwt_required()
    def put(self, id):
        dados = argumentos.parse_args()
        if dados.get('ativado') is None:
            return {"message": "The field 'ativado' cannot be left blank"}, 400

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
        if not dados.get('email') or dados.get('email') is None:
            return {"message": "The field 'email' cannot be left blank"}, 400

        if UserModel.find_by_email(dados['email']):
            return {"message": "The email '{}' already exists.".format(dados['email'])}, 400

        if UserModel.find_by_email(dados['email']):
            return {"message": "The email '{}' already exists.".format(dados['email'])}
        user = UserModel(**dados)
        user.ativado = False
        try:
            user.save_user()
            user.send_confirmation_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {'message': 'An internal server error has ocurred'}, 500
        return {'message': 'User created sucessfully!'}, 201

class UserDelete(Resource):
    
    @jwt_required()
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
            if user.ativado:
                token_de_acesso = create_access_token(identity=user.id)
                return {'acess_token': token_de_acesso}, 200
            return {'message': 'User not confirmed.'}
        return {'message': 'The username or password is incorrect.'}, 401

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] #JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200

class UserConfirm(Resource):
    #raiz_do_site/confirmacao/{user_id}
    @classmethod
    def get(cls, id):
        user = UserModel.find_user(id)

        if not user:
            return {"message": "User id '{}' not found.".format(id)}, 404

        user.ativado = True
        user.save_user()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('user_confirm.html', email=user.email), 200, headers)