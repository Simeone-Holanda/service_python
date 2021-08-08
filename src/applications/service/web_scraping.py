import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from src.util.settings import REQUISICOES
from src.infrastructure.db_factory import DBStart
from src.infrastructure.entities import Approveds
from src.infrastructure.repository import UserRepository

MAX_THREADS = 30

class WebScraping:
    """ Pega todos os dados do site e salva no banco de dados"""

    def __init__(self) -> None:
        DBStart.start_db()
        self.req = requests.session()
        self.db = UserRepository()

    def run(self):
        """
        Cria todas as urls dos sites que vai ser extraido os dados.
        Exemplo das urls:
            - https://sample-university-site.herokuapp.com/approvals/1
            - https://sample-university-site.herokuapp.com/approvals/2

        [NOTE] : Temos cerca de 4671 urls com 10 urls dentro de cada um ou seja 10 aprovados por site.
                Devido ao número de requisições foi usado thread junto a outras tecnicas para melhorar a
                velocidade das requisições. Ainda sim foi encontrado um certo problema na questão do tempo,
                Alguns dos tempos atingidos foram:
                - 94.13 segundos para  1000 requisições com 10 usuarios em cada
                - 113.16 segundos para  1000 requisições com 10 usuarios em cada
                - 129.11 segundos para  1000
        """

        inicio = time.time()
        lista_values_sites = [x for x in range(1,REQUISICOES+1)]
        base_url = 'https://sample-university-site.herokuapp.com/approvals/'
        list_urls = map(lambda x: base_url+str(x),lista_values_sites)
        threads = min(MAX_THREADS, len(lista_values_sites))
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(self.__get_all_data,list_urls)
        final = time.time()
        print(round(final-inicio,2), "segundos para ", len(lista_values_sites))

    def __get_name_score(self,url):
        """ Pega o cpf, nome e score do vestibulando cria um Approved() e inseri no banco de dado. """
        session = self.req.get(url)
        soup = BeautifulSoup(session.content,'html.parser')
        divs = soup.find_all('div')
        cpf = url.split('/')[-1]
        name = divs[0].contents[1]
        score= divs[1].contents[1]
        new_data = Approveds(cpf=cpf,name=name,score=score)
        self.db.save(new_data)

    def __get_all_data(self,page_espec):
        """
        Cria todas as urls referente aos vestibulando e faz o web scraping de cada uma delas
        exemplo:
            https://sample-university-site.herokuapp.com/candidate/876.520.413-17 - [cpf- 876.520.413-17]
        """

        base_url = 'https://sample-university-site.herokuapp.com/'
        session = self.req.get(page_espec)
        soup = BeautifulSoup(session.content,'html.parser')
        tag_cpf = soup.select('li a')
        list_cpf = [x.next_element for x in tag_cpf]
        urls = [base_url+"candidate/"+cpf for cpf in list_cpf] # urls do site
        threads = min(MAX_THREADS, len(urls))
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(self.__get_name_score, urls)
