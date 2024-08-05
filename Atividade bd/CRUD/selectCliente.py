import conexao1
import sqlite3

def exibirClientes():
    conexao1.conectar()
    resultado = conexao1.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("######################")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF: ",result[3])
        print("Telefone: ",result[4])
        print("Endereço: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
    #conexao1.conn.close()


def consultarClientes():
    conexao1.conectar()
    cpf = input("Informe o CPF que deseja Consultar: ")
    try:
        resultado = conexao1.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
                print("CPF não encontrado!")
        #print("Cliente encontrado ",resultado)
        else:
            for result in resultado:
                print("##########################################")
                print("Nome: ",result[0])
                print("Sobrenome: ",result[1])
                print("Idade: ",result[2])
                print("CPF: ",result[3])
                print("Telefone: ",result[4])
                print("Endereço: ",result[5])
                print("Cidade: ",result[6])
                print("Estado: ",result[7])
            #print("Cliente encontrado: ",resultado)
                return cpf
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    #conn.close()