from flask import Flask
from flask_restful import Api
from resources.user import Users, User

app = Flask(__name__)
api =  Api(app)

#Adicionar o recurso. Colocar o nome da classe e da onde quer que seja chamado.
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

#Se o nome for o principal (app.py), rode o arquivo
if __name__ == '__main__':
    app.run(debug=True) #Esse debug é True só enquanto estiver em produção