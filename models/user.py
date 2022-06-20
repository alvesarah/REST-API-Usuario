from sql_alchemy import banco
from flask import request, url_for
from requests import post

MAILGUN_DOMAIN = 'sandboxe9340a4b5cf24f88aaa53c3f340c7fef.mailgun.org'
MAILGUN_API_KEY = '731319d37f0d7d51b76989c5577e3f04-4f207195-8a6694aa'
FROM_TITLE = 'NO-REPLY'
FROM_EMAIL = 'no-reply@restapi.com'

class UserModel(banco.Model):

    __tablename__ = 'users'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    email = banco.Column(banco.String(100), nullable=False, unique=True)
    telefone = banco.Column(banco.Integer)
    senha = banco.Column(banco.String(40))
    ativado = banco.Column(banco.Boolean, default=False)

    def __init__(self, nome, email, telefone, senha, ativado):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.ativado = ativado

    def send_confirmation_email(self):
        link = request.url_root[:-1] + url_for('userconfirm', id=self.id)
        return post('https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
        auth=('api', MAILGUN_API_KEY),
        data={'from': '{} <{}>'.format(FROM_TITLE, FROM_EMAIL),
        'to': self.email,
        'subject': 'Confirmação de Cadastro',
        'text': 'Confirme seu cadastro clicando no link a seguir: {}'.format(link),
        'html': '<html><p>Confirme seu cadastro clicando no link a seguir: <a href="{}">CONFIRMAR EMAIL</a></p></html>'.format(link)})

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'ativado': self.ativado
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