from flask import Flask
from flask_restful import Api
from resources.user import Users, User, UserDelete, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api =  Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserDelete, '/delete_user/<int:id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)