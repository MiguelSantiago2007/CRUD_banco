import sqlite3

def conectar():
    try:
        #global banco
        banco = sqlite3.connect('primeiro_banco.db')
        #global cursor
        cursor = banco.cursor()
        print("Operação concluida")
    except sqlite3.Error as erro:
        print("Erro de Conexão")