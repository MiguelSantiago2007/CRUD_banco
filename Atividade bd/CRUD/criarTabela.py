import sqlite3
import conexao1

#Criação de tabela Clientes
conexao1.conectar()
def criar():
    criar_tabela = "CREATE TABLE IF NOT  EXISTS cliente(nome string, sobrenome string, idade integer, cpf integer, telefone integer, endereco string, cidade string, estado string)"
    conexao1.cursor.execute(criar_tabela)