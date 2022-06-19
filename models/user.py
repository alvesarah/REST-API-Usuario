from sql_alchemy import banco
class UserModel(banco.Model):

    __tablename__ = 'users'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    email = banco.Column(banco.String(100))
    telefone = banco.Column(banco.Integer)
    senha = banco.Column(banco.String(40))

    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
        }

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None
    
    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None


    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def update_user(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()