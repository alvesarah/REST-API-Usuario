from flask_restful import Resource, reqparse
from models.user import UserModel
#reqparse -> Receber os elementos JSON da nossa requisição, todos os argumentos

users = [
    {
        'id': 1,
        'nome': 'Maria',
        'email': 'maria@hotmail.com',
        'telefone': 11912342345
    },
    {
        'id': 2,
        'nome': 'João',
        'email': 'joao@hotmail.com',
        'telefone': 11912342346
    }
]

#Recurso da nossa API (get, post, put e delete)
class Users(Resource):
    def get(self):
        return {'users': users}

class User(Resource):   
    argumentos = reqparse.RequestParser()
    #Ele só vai aceitar a alteração dos argumentos abaixo
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('telefone')

    def find_user(id):
        for user in users:
            if user['id'] == id:
                return user
        return None

    def get(self, id):
        user = User.find_user(id)
        if user:
            return user
        return {'message': 'User not found.'}, 404 #not found

    def post(self, id):
        #Chave e valor de todos os argumentos passados
        dados = User.argumentos.parse_args()
        user_objeto = UserModel(id, **dados)
        novo_user = user_objeto.json()
        
        users.append(novo_user)
        return novo_user, 200

    def put(self, id):
        dados = User.argumentos.parse_args()
        user_objeto = UserModel(id, **dados)
        novo_user = user_objeto.json()

        user = User.find_user(id)
        if user:
            user.update(novo_user)
            return novo_user, 200 #OK
        users.append(novo_user)
        return novo_user, 201 #created

    def delete(self, id):
        #Esse users que estamos referenciando, é a lista de users que ja foram criadas
        global users
        users = [user for user in users if user['id'] != id]
        return {'messagem': 'User deleted.'}