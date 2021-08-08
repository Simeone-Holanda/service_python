# Bot service

## Prerequisites
- <a href="https://www.apachefriends.org/pt_br/index.html"> MySQL</a> **Site do xampp**
- <a href="https://www.python.org/downloads/">Python3</a> - **Recomendado adicionar o python ao path do sistemas quando for fazer o download**

## Getting Started
1. **Clone this repository**

   ```
   git clone https://github.com/Simeone-Holanda/service_python.git
   ```
   ```
   cd service_python
   ```
2. **Set up your mysql** <br>
    <p>Recomendo usar o xampp pela sua facilidade de configuração do mysql. Em seguida abra seu xampp e inicie os serviços do apache e do mysql, apos isso va até o arquivo settings.py no seguinte caminho cd/service_python/util/settings.py e adicione suas configurações para a conexão com o database e as demais constantes do projeto.</p>

   * Configurações padrão do arquivo setting.py :

     HOST = 'localhost'<br>
     USER = 'root'<br>
     PASSWD = ''<br>
     DB_NAME='name_db'<br><br>

3. **Create and enter in your virtual environment** <br>
    Este passo é **opcional**, porém é recomendado para manter o projeto com suas dependencias e bibliotecas separados dos demais projetos que possa haver, onde ele será executado.
    ```
    pip3 install virtualenv
    ```
    ```
    python3 -m virtualenv venv
    ```
4. **Install all used libraries** <br>  
   ```
   pip3 install -r requirements.txt
   ```
5. **Execute the service**
   ```
   python3 service.py
   ```

