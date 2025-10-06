from util import *
from tabulate import tabulate

def entrar_operacao():
    while True:
        oper = input("Entre com [C]rédito ou [D]ébito: ").upper()
        if (oper not in ["C", "D"]):
            print("Erro: operação inválida")
        else:
            break
    return oper

def realizar_operacao(oper, valor, conta):
    if (oper == "C"):
        conta[2] += valor
    elif (oper == "D"):
        conta[2] -= valor

def alterar_conta(contas):
    id = entrar_inteiro("Entre com o id: ")
    conta = pesquisar_conta(contas, id)
    if (not conta):
        print("Erro: conta não exite")
        return
    nome = entrar_nome()
    oper = entrar_operacao()
    valor = entrar_valor()
    realizar_operacao(oper, valor, conta)

def incluir_conta(contas):
    id = entrar_inteiro("Entre com o id: ")
    conta = pesquisar_conta(contas, id)
    if conta:
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    contas.append([id, nome, saldo])

def excluir_conta(contas):
    id = entrar_inteiro("Entre com o id: ")
    conta = pesquisar_conta(contas, id)
    if (not conta):
        print("Erro: conta não exite")
        return
    contas.remove(conta)

def consultar_contas(contas):
    tabela = [["Id", "Nome", "Saldo"]]
    for conta in contas:
        tabela.append(conta)
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))

def consultar_conta(contas):
    id = entrar_inteiro("Entre com o id: ")
    conta = pesquisar_conta(contas, id)
    if not conta:
        print("Erro: conta não existe")
        return
    tabela = [["Id", "Nome", "Saldo"]]
    tabela.append(conta)
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))