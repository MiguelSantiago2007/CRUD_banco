import sqlite3
import conexao1
def Atualizar():
    conexao1.conectar()
    import sqlite3

    nome = input("Informe seu nome: ")
    sobrenanome = input("Informe o Sobrenome: ")
    idade = int(input("Informe sua idade: "))
    cpf = int(input("Informe o CPF: "))
    telefone = int(input("Informe o Nº de Telefone: "))
    endereco = input("Informe seu Endereço: ")
    cidade = input("Informe a Cidade: ")
    estado = input("Informe o estado: ")
        
    inserircliente = "UPDATE pessoas SET ('"+nome+"', '"+sobrenanome+"', '"+str(idade)+"', '"+str(cpf)+"', '"+str(telefone)+"', '"+endereco+"', '"+cidade+"', '"+estado+"')"
    conexao1.cursor.execute(inserircliente)
    conexao1.conn.commit()

    banco = sqlite3.connect('cadastro.db')

    cursor = banco.cursor()

    banco.commit() 
    
    """cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())"""