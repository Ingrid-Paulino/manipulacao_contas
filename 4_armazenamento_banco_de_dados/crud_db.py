from conexao import *
from models import Conta

def incluir_conta_db(conta):
    comando = "insert into conta (nome, saldo) values (%s, %s);"
    try:
        conn = conectar()
        cursor = conn.cursor() # cursor permite acessar o banco
        cursor.execute(comando, (conta.nome, conta.saldo))
        conn.commit() #commit implementa a inserssão do dado
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def alterar_conta_db(conta):
    comando = "update conta set nome = %s, saldo = %s where id = %s;"
    try:
        conn = conectar()
        cursor = conn.cursor() # cursor permite acessar o banco
        cursor.execute(comando, (conta.nome, conta.saldo, conta.id))
        conn.commit() #commit implementa a modificação no banco
    except Exception as ex:
        print(ex)
    finally: #executa independente do try ou except
        desconectar(conn)

def excluir_conta_db(conta):
    comando = "delete from conta where id = %s;"
    try:
        conn = conectar()
        cursor = conn.cursor()# cursor permite acessar o banco
        cursor.execute(comando, (conta.id,))
        conn.commit() #commit implementa o delete
    except Exception as ex:
        print(ex)
    finally: #executa independente do try ou except
        desconectar(conn)

def consultar_conta_db(id):
    comando = "select * from conta where id = %s;" #no sql lite o %s é ?(interrogação)
    contas = None
    try:
        conn = conectar()
        cursor = conn.cursor() # cursor permite acessar o banco
        cursor.execute(comando, (id,)) #pos o id tem que ter virgula para o python entender que é uma tupla a estrutura do dado
        registro = cursor.fetchone() #busca um unico registro
        if registro:
            conta = Conta(registro[0], registro[1], registro[2])
    except Exception as ex:
        print(ex)
    finally: #executa independente do try ou except
        desconectar(conn)
    return conta 

def consultar_contas_db():
    comando = "select * from conta;"
    contas = []
    try:
        conn = conectar()
        cursor = conn.cursor() # cursor permite acessar o banco
        cursor.execute(comando)
        registros = cursor.fetchall() #acessa todos os registros da tabela conta
        #registros é retornado em tuplas
        for registro in registros:
            contas.append(Conta(registro[0], registro[1], registro[2]))
    except Exception as ex:
        print(ex)
    finally: #executa independente do try ou except
        desconectar(conn)
    return contas