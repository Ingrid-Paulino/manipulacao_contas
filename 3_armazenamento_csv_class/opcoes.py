from crud import *
from arquivo import *
from menu import *

FIM = 0
contas = ler_contas()
print(contas)
opcao = entrar_opcao()
while (opcao != FIM):
    match (opcao):
        case 1: incluir_conta(contas)
        case 2: alterar_conta(contas)
        case 3: excluir_conta(contas)
        case 4: consultar_conta(contas)
        case 5: consultar_contas(contas)
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
gravar_contas(contas)