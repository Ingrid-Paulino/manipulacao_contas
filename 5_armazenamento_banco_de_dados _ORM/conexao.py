from sqlalchemy import create_engine
  #pip install sqlalchemy
  #pip install pymsql
from sqlalchemy.orm import sessionmaker
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
    session = None
    try: #coneção com sqlalchemy
		   engine = create_engine("mysql+pymysql://{username}:{password}@{host}/{database}"
					.format(user=params.get("DB", "username"),
	        password=params.get("DB", "password"), 
	        host=params.get("DB", "host"), 
					database=params.get("DB", "database"))
			)
			session = sessionmaker(bind = engine)()
    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if session:
        session.close()

# testa conecção   
#session = conectar()
#desconectar(conn)