import sqlite3
import conexao1

def deletar():
    cpf = input("Informe o CPF que deseja deletar: ")
    try:
        resultado = conexao1.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        #print("Cliente encontrado ",resultado)
        else:
            conn = sqlite3.connect('cadastro.db')

            cursor = conn.cursor()

            cursor.execute("DELETE from cliente WHERE cpf = '"+cpf+"' ")

            conn.commit()
            
            print("Os dados foram removidos com suceso!!")
    except sqlite3.Error as erro:
                print("Erro ao Excluir: ",erro)