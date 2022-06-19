import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTOINCREMENT, nome text, email text, telefone int)"

cria_user = "INSERT INTO users VALUES (1, 'Sarah Alves', 'salves726@gmail.com', 11968426001)"

cursor.execute(cria_tabela)
cursor.execute(cria_user)
connection.commit()
connection.close()