import sqlite3
import conexao1
import selectCliente

def Atualizar():
    conexao1.conectar()
    global cpfpesquisar
    
    cpf = input("Informe o CPF que deseja Consultar: ")
    try:
        resultado = conexao1.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
                print("CPF não encontrado!")
        #print("Cliente encontrado ",resultado)
        else:
            #for result in resultado:
            idade = int(input("\nInforme sua idade: "))
            telefone = int(input("Informe o Nº de Telefone: "))
            endereco = input("Informe seu Endereço: ")
            cidade = input("Informe a Cidade: ")
            estado = input("Informe o estado: ")
        
            atualizarcliente = "UPDATE cliente SET idade = '"+str(idade)+"',telefone = '"+str(telefone)+"',endereco = '"+endereco+"',cidade = '"+cidade+"',estado = '"+estado+"'"
            conexao1.cursor.execute(atualizarcliente)
            
            #cursor = conexao1.conn.cursor()
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    conexao1.conn.commit() 
    """cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())"""
    