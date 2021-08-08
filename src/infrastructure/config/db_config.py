from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.util.settings import USER, PASSWD, DB_NAME, HOST

class DBConnection:

    def __init__(self) -> None:
        """ Adicionar as variaveis padrao!"""
        self.__connection = "mysql+pymysql://{}{}@{}/{}".format(USER,PASSWD,HOST,DB_NAME)
        self.session = None

    def get_engine(self):
        """ Criando nossa engine"""
        engine = create_engine(self.__connection)
        return engine

    def set_session(self):
        """ Criando nossa engine e a session. Foi usado o scoped_session para que ele gerencie a quantidade de session e requisiçoes
            que irão vim por conta das threed.
        """
        engine = create_engine(self.__connection,pool_size=15, max_overflow=30)
        session_maker = sessionmaker(bind=engine) 
        self.session = scoped_session(session_maker)
        return self

    