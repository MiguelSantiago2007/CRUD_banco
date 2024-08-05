import sqlite3
import conexao1

#Criando uma Função Para Coletar dados do Clientes
def cadastrar():
    try:
        conexao1.conectar()
        nome = input("Informe seu nome: ")
        sobrenanome = input("Informe o Sobrenome: ")
        idade = int(input("Informe sua idade: "))
        cpf = int(input("Informe o CPF: "))
        telefone = int(input("Informe o Nº de Telefone: "))
        endereco = input("Informe seu Endereço: ")
        cidade = input("Informe a Cidade: ")
        estado = input("Informe o estado: ")
        
        inserircliente = "INSERT INTO cliente VALUES ('"+nome+"', '"+sobrenanome+"', '"+str(idade)+"', '"+str(cpf)+"', '"+str(telefone)+"', '"+endereco+"', '"+cidade+"', '"+estado+"')"
        conexao1.cursor.execute(inserircliente)
        conexao1.conn.commit()
        conexao1.conn.close()
        print("CLIENTE CADASTRADO COM SUCESSO")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar cliente",erro)