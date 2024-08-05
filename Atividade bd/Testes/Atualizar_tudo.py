import sqlite3
import conecta

def Atualizar():
    conexao1.conectar()
    import sqlite3

    cpf = input("Informe o CPF que deseja Consultar: ")
    try:
        resultado = conexao1.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
                print("CPF não encontrado!")
        #print("Cliente encontrado ",resultado)
        else:
            #for result in resultado:
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
                
                novo_nome = input("\nInforme o novo nome: ")
                novo_sobrenome = input("\nInforme o novo Sobrenome: ")
                novo_cpf = int(input("\nInforme o novo CPF: "))
                nova_idade = int(input("\nInforme a nova idade: "))
                novo_telefone = int(input("Informe o Nº de Telefone: "))
                novo_endereco = input("Informe seu Endereço: ")
                nova_cidade= input("Informe a Cidade: ")
                novo_estado = input("Informe o estado: ")
                
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE cliente SET Nome = '"+novo_nome+"',Sobrenome = '"+novo_sobrenome+"'Idade = '"+nova_idade+"',CPF = '"+novo_cpf+"',Telefone = '"+novo_telefone+"',Endereco = '"+novo_endereco+"',Cidade = '"+nova_cidade+"',Estado = '"+novo_estado+"'")
        
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    conn.commit() 
    
    """cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())"""
    


    