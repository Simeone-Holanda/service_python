from pymysql import connect
from pymysql.err import ProgrammingError
from src.infrastructure.config import Base, DBConnection
from src.util.settings import USER, PASSWD, DB_NAME, HOST


class DBStart():

    @classmethod
    def start_db(self):
        """
        Cria a nossa base de dados, caso ja exista e nos retorna um erro ProgrammingError, 
        seguiremos normalmente usando a base de dados que ja tem criada.
        """
        try:
            connection = connect(
                host= HOST,
                user= USER,
                passwd= PASSWD
            )
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE {}".format(DB_NAME))
        except ProgrammingError:
            print("Database already exists.")
            pass
        db_conn = DBConnection()
        engine = db_conn.get_engine()
        Base.metadata.create_all(engine)