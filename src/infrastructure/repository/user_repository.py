from src.infrastructure.entities import Approveds
from src.infrastructure.config import DBConnection
from src.infrastructure.entities import Approveds 
from sqlalchemy.orm.exc import NoResultFound


class UserRepository:

    def __init__(self) -> None:
        """ Como estamos trabalhando com threed definimos uma unica sessão para o scoped_session fazer o controle de sessões e entradas
            de requisições.
        """
        self.db_conn = DBConnection().set_session()

    def save(self,new_data: Approveds) -> Approveds:
        """ Faz a validação do cpf e a higienização de dados antes de inserir"""
        try: 
            new_data.validate_cpf()
            new_data.clear_field_name()
            self.db_conn.session.add(new_data) 
            self.db_conn.session.commit()
        except Exception as ex:
            print(ex)
            self.db_conn.session.rollback()
            raise Exception("Erro in the method save()")
        finally:
            self.db_conn.session.remove()

    def find_data(self,cpf : str = None, name : str = None):
        """ Realiza uma busca no banco de dados por um nome ou cpf
            param: 
                - [cpf] cpf do usuário que se encontra no banco de dado.[Opcional]
                - [name] nome do usuário que se encontra no banco de dados.[Opcional]
        """

        try:
            if cpf is None:
                return self.db_conn.session.query(Approveds).filter_by(name=name).one()
            elif name is None:
                return self.db_conn.session.query(Approveds).filter_by(cpf=cpf).one()
            else:
                raise ValueError("Enter the cpf or name of the data you want to search.")
        except NoResultFound:
            return None
        except Exception as ex:
            self.db_conn.session.rollback()
            raise ex
        finally:
            self.db_conn.session.remove()




    



