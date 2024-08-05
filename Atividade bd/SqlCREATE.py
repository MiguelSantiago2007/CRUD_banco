import sqlite3

def CREATE():

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("CREATE TABLE cliente VALEU (nome text, idade integer, email text)")

    banco.commit() 
    