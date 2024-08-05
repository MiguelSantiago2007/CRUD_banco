import sqlite3
import Conexao
def INSERIR():
    Conexao.conectar()
    Conexao.banco = sqlite3.connect('primeiro_banco.db')

    Conexao.cursor = Conexao.banco.cursor()

    Conexao.cursor.execute("INSERT INTO pessoas VALUES ('pedro',20,'pedro@gmail.com')")

    Conexao.banco.commit() 
    Conexao.cursor.execute("SELECT * FROM pessoas")
    print(Conexao.cursor.fetchall())