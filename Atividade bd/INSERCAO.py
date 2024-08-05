import sqlite3
import Conexao
def INSERIR():

    try:
        Conexao.conectar()
        nome = input("Qual nome a ser inserido? ")
        idade = input("Idade a ser inserida? ")
        email = input("Email a ser inserido? ")
        Conexao.banco = sqlite3.connect('primeiro_banco.db')

        Conexao.cursor = Conexao.banco.cursor()

        Conexao.cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"','"+idade+"','"+email+"'")

        Conexao.banco.commit() 
    except Exception as e:
        print("Erro a inserir dados", e)
        Conexao.cursor.execute("SELECT * FROM pessoas")
        print(Conexao.cursor.fetchall())