import sqlite3
from funcaoMenu import menu
import conexao1
import criarTabela
import cadastrarClientes
import selectCliente
import atualizarDados
import deletarcliente

#Criação da Tabela Cliente
criarTabela.criar()

opcao = menu()
while (opcao !='6'):

    if(opcao == '1'):
        cadastrarClientes.cadastrar()
    elif(opcao == '2'):
        selectCliente.exibirClientes()
    elif(opcao == '3'):
        selectCliente.consultarClientes()
    elif(opcao == '4'):
        atualizarDados.Atualizar()
    elif(opcao == '5'):
        deletarcliente.deletar()
    opcao = menu()
