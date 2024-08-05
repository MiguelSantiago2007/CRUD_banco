import sqlite3
#Criação da função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn = sqlite3.connect("cadastro.db")
        global cursor
        cursor = conn.cursor()
        print("Conexão com Banco realiada com sucesos!")
    except sqlite3.Error as erro:
        print("Erro de Conexão com o Banco de Dados")