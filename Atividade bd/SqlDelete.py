import sqlite3

def deletar():

    try:
        banco = sqlite3.connect('primeiro_banco.db')

        cursor = banco.cursor()

        cursor.execute("DELETE from pessoas WHERE cpf ")

        banco.commit()
    
        print("Os dados foram removidos com suceso!!")

    except sqlite3.Error as erro:
        print("Erro ao Excluir: ",erro)