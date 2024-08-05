def menu():
    print("###################---- TABELA DE CLIENTES ----###########################")
    print("Oque deseja fazer: ")
    print(""" 1 - CADASTRAR CLIENTES:
          \n 2 - EXIBIR CLIENTES:
          \n 3 - CONSULTAR CLIENTES PELO CPF:
          \n 4 - ALTERAR DADOS CADASTRAIS:
          \n 5 - EXCLUIR CLIENTES:
          \n 6 - SAIR""")
    print("####################---- FIM DA TABELA ----############################")
    global opcao
    opcao = input()
    return opcao