from sql_alchemy import banco
class UserModel(banco.Model):

    __tablename__ = 'users'

    id = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String(80))
    email = banco.Column(banco.String(100))
    telefone = banco.Column(banco.Integer)

    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def update_user(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone