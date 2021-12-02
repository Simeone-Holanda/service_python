# Web Scraping


## Fluxo e captura de dados
   <p> Todo o fluxo está documentado no arquivo web_scraping, onde cada método descreve sua função no processo.</p>

## Estratégias para acelerar o processo de captura de dados:
   * Bilioteca concurrent.futures para usar multithreading e fazer varias requisições ao mesmo tempo.
   * Criar uma sessões de requests geral para tratar todos os requests.
   * Aumentar a quantidade threed que vai ser usado, para isso acabei tendo que definir a alguns paramentros a mais na criação da engine e sessions do sqlalchemy.

## Prerequisites
- <a href="https://www.apachefriends.org/pt_br/index.html"> MySQL</a> **Site do xampp**
- <a href="https://www.python.org/downloads/">Python3</a> - **Recomendado adicionar o python ao path do sistemas quando for fazer o download**

## Começando
1. **Clone este repositório**

   ```
   git clone https://github.com/Simeone-Holanda/service_python.git
   ```
   ```
   cd service_python
   ```
2. **Configure seu MySQL** <br>
    <p>Recomendo usar o xampp pela sua facilidade de configuração do mysql. Em seguida abra seu xampp e inicie os serviços do apache e do mysql, apos isso va até o arquivo settings.py no seguinte caminho cd/service_python/util/settings.py e adicione suas configurações para a conexão com o database e as demais constantes do projeto.</p>

   * Configurações padrão do arquivo setting.py :

     HOST = 'localhost'<br>
     USER = 'root'<br>
     PASSWD = ''<br>
     DB_NAME='name_db'<br><br>
   * Aproveitando que estamos aqui vamos configurar a quantidade de sites que iremos obter os  dados e a quantidade de threed que queremos.Essas configurações são preferencias minhas <br>
   SITES_WITH_USERS = 4671<br>
   MAX_THREED = 200<br>
   

3. **Crie e entre em um ambiente virtual** <br>
    Este passo é **opcional**, porém é recomendado para manter o projeto com suas dependencias e bibliotecas separados dos demais projetos que possa haver, onde ele será executado.
    ```
    pip3 install virtualenv
    ```
    ```
    python3 -m virtualenv venv
    ```
4. **Instale todas as bibliotecas necessarias para a execução do programa** <br>  
   ```
   pip3 install -r requirements.txt
   ```
5. **Execute o serviço**
   ```
   python3 service.py
   ```

