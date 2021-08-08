import unicodedata
from sqlalchemy import Column, String
from src.infrastructure.config import Base

class Approveds(Base):
    __tablename__ = 'approveds'

    cpf = Column(String(length=50), primary_key=True)
    name = Column(String(length=50))
    score = Column(String(length=50))

    def __repr__(self) -> str:
        return f"cpf: {self.cpf}, nome:{self.name}, score: {self.score}"

    def clear_field_name(self): 
        """ Retira acentos e converte letras de maiúsculo em minúsculo"""
        self.name = self.name.lower()
        palavra = unicodedata.normalize('NFKD', self.name)
        self.name = u"".join([c for c in palavra if not unicodedata.combining(c)])
    
    def validate_cpf(self):
        """ Verifica se o cpf contem apenas numeros, caso não dispara uma exceção"""

        cpf = self.cpf.replace("-",".")
        cpf_splited = cpf.split('.')
        for digito in cpf_splited:
            if not digito.isnumeric():
                raise ValueError("Cpf deve conter apenas números.")
                
