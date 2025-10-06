from util import *
from tabulate import tabulate
from models import Conta
from crud_db import *

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
        conta.saldo += valor
    elif (oper == "D"):
        conta.saldo -= valor

def alterar_conta():
    id = entrar_inteiro("Entre com o id: ")
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não exite")
        return
    conta.nome = entrar_nome()
    oper = entrar_operacao()
    valor = entrar_valor()
    realizar_operacao(oper, valor, conta)
    alterar_conta_db(conta)

def incluir_conta():
    nome = entrar_nome()
    saldo = entrar_saldo()
    incluir_conta_db(Conta(None, nome, saldo))

def excluir_conta():
    id = entrar_inteiro("Entre com o id: ")
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não exite")
        return
    excluir_conta_db(conta)

def consultar_contas():
    tabela = [["Id", "Nome", "Saldo"]]
    contas = consultar_contas_db()
    for conta in contas:
        tabela.append(conta.retornar_lista())
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))

def consultar_conta():
    id = entrar_inteiro("Entre com o id: ")
    conta = consultar_conta_db(id)
    if not conta:
        print("Erro: conta não existe")
        return
    tabela = [["Id", "Nome", "Saldo"]]
    tabela.append(conta.retornar_lista())
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
        