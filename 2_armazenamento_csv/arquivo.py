import os.path

#forma 1
#ARQ = "C:\\Users\\1pmaia\\Desktop\\Python\\Turma-Python-N\\Aula13\\contas.csv" #as barras duplicas faz o python não interpretar as barras como caracter de controle
#forma 2
#ARQ = r"C:\Users\1pmaia\Desktop\Python\Turma-Python-N\Aula13\contas.csv" #a letra é faz o python não interpretar as barras como caracter de controle

#forma 3
ARQ = "contas.csv"
DIR = os.path.dirname(os.path.abspath(__file__))#busca o arquivo em qualquer lugar/diretorio que esteja o meu csv
ARQ = os.path.join(DIR, ARQ)

def ler_contas():
	contas = []
	try:
		with open(ARQ, mode="r", encoding="UTF-8") as arq: #abri o arquivo para leitura no formato utf-8
			for linha in arq:
				campos = linha.split(",")
				id, nome, saldo = int(campos[0]), campos[1], float(campos[2]) #atribuição multiplica
				contas.append([id, nome, saldo])
	except Exception as ex:
		print(ex)
	return contas
	
	
	
	def gravar_contas(contas):
		try:
			with open(ARQ, mode="w", encoding="UTF-8") as arq:
				for conta in contas:
					 arq.write(f"{conta[0]}, {conta[1]}, {conta[2]}\n")
		
	except Exception as ex:
		print(ex)