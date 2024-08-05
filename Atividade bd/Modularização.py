import SqlCREATE
import INSERCAO
import SqlDelete
import SqlUPDATE
import Conexao


print("Informe a operação 1-Criar/2-Inserir/3-Deletar/4-Atualizar")
opcao = int(input('Qual função deseja realizar: '))

if(opcao == 1):
   
    Conexao.conectar
    SqlCREATE.CREATE()

elif(opcao == 2):
    
    Conexao.conectar
    INSERCAO.INSERIR()

elif(opcao == 3):
    
    Conexao.conectar
    SqlDelete.deletar()

elif(opcao == 4):
   
    Conexao.conectar
    SqlUPDATE.Atualizar()

else:
    exit