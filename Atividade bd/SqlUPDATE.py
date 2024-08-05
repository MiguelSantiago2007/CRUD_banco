import sqlite3
import conexao1
#def Atualizar():
conexao1.conectar()
import sqlite3

nome = "Adolph"
idade = 888
    #email = "pedro@gmail.com"

banco = sqlite3.connect('cadastro.db')

cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'Tarciso' WHERE idade = 888")

banco.commit() 
    
"""cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())"""