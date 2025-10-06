NUM_NOMES = 2
MIN_NOME = 2
MIN_SOBRENOME= 2

def pesquisar_conta(contas, id):
    conta_procurada = []
    for conta in contas:
        if (conta[0] == id):
            conta_procurada = conta
            break
    return conta_procurada

def entrar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break # se não houver erro
        except Exception:
            print("Erro: valor inválido")
    return num

def entrar_real(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except Exception:
            print("Erro: valor inválido")
    return num

def entrar_valor():
    while True:
        valor = entrar_real("Entre com o valor: ")
        if (valor > 0):
            break
        else:
            print("Erro: valor inválido")
    return valor

def entrar_saldo():
    while True:
        saldo = entrar_real("Entre com o saldo: ")
        if (saldo >= 0):
            break
        else:
            print("Erro: saldo inválido")
    return saldo

def validar_nome(nome):
    return (len(nome) >= NUM_NOMES)

def validar_nome_sobrenome(nome):
    return (len(nome[0]) >= MIN_NOME and len(nome[1]) >= MIN_SOBRENOME)

def entrar_nome():
    while True:
        nome = input("Entre com um nome: ")
        nome_sobrenome = nome.split(" ")
        if validar_nome(nome_sobrenome):
            if validar_nome_sobrenome(nome_sobrenome):
                break
            else:
                print("Erro: nome e sobrenome devem ter mais de dois caracteres")
        else:
            print("Erro: nome inválido pq precisa de nome e sobrenome")
    return nome