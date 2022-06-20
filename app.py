from flask import Flask, jsonify
from flask_restful import Api
from blacklist import BLACKLIST
from resources.user import Users, User, UserPut, UserPost, UserDelete, UserLogin, UserLogout, UserConfirm
from flask_jwt_extended import JWTManager
from sql_alchemy import banco
from flask import render_template, make_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
banco.init_app(app)
api =  Api(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'), headers)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def  verifica_blacklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserPut, '/edit_user/<int:id>')
api.add_resource(UserPost, '/add_user')
api.add_resource(UserDelete, '/delete_user/<int:id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserConfirm, '/confirmacao/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)