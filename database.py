#Importar o sqlite
import sqlite3

#Criar o banco:
conexao = sqlite3.connect('estoque.db')

#Criar a tabela Produto:
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,     
        produto TEXT NOT NULL,
        valor REAL NOT NULL
    )
''')

#Salvar o banco no estoque.db
conexao.commit()
conexao.close()
print("Banco e tabela prontos.")