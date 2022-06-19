from flask import Flask
from flask_restful import Api
from resources.user import Users, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api =  Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)