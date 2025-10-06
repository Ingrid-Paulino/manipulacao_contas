from util import entrar_inteiro

OPCOES = (0, 1, 2, 3, 4, 5)

def exibir_menu():
    print("[1] - Incluir")
    print("[2] - Alterar")
    print("[3] - Excluir")
    print("[4] - Consultar conta")
    print("[5] - Consultar contas")
    print("[0] - Sair")
    
def entrar_opcao():
    while True:
        exibir_menu()
        opcao = entrar_inteiro("Entre com a opçao: ")
        if opcao not in OPCOES:
            print("Erro: opção inválida")
        else:
            break
    return opcao