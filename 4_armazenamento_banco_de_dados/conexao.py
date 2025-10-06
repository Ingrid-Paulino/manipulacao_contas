# import mysql.connector # para conectar ao banco é necessario esse pacote
  #pip install mysql-connector-python

##forma 1
# def conectar():
#     conn = None
#     try:
#          -g     - - -  
# -  conn = mysql.connector.connect(user="root", password="lpmaia", database="banco")
#     except Exception as ex:
#         print(ex)
#     return conn

# def desconectar(conn):
#     if conn:
#         conn.close()

# testa conecção   
#conn = conectar()
#desconectar(conn)

##forma 2 com variaveis de ambiente
import mysql.connector # para conectar ao banco é necessario esse pacote
  #pip install mysql-connector-python

import pathlib
import os.path
import configparser

ARQ = "local.env"
DIR = pathlib.Path(__file__).parent.resolve()
ARQ = os.path.join(DIR, ARQ)

def ler_arquivo_config():
	params = configparser.ConfigParse()
	params.read(ARQ)
	return params
	

def conectar():
    conn = None
    try:
		   conn = mysql.connector.connect(
	        user=params.get("DB", "username"),
	        password=params.get("DB", "password"), 
	        host=params.get("DB", "host"), 
	        port=params.get("DB","port"),
					database=params.get("DB", "database")
			)
    except Exception as ex:
        print(ex)
    return conn

def desconectar(conn):
    if conn:
        conn.close()

# testa conecção   
#conn = conectar()
#desconectar(conn)