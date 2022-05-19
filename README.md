# sd-tp

### Pré-requisitos
1. [Python](https://www.python.org/downloads/)
2. [Pip] (https://pip.pypa.io/en/stable/installation/)
3. [PostgreSQL](https://www.postgresql.org/download/)

** É recomendado a execução do python em [venv](https://docs.python.org/3/tutorial/venv.html);

### Pacotes necessários
Acesse o diretório dentro do projeto clonado: hugo_sd_tp
Existe um arquivo chamado requirements.txt, nele estão todas as dependências do projeto.

Para instalar as dependências:
```sh
$ pip install -r requirements.txt
```

### Como executar
1. Crie um schema para a aplicação no seu servidor PostgreSQL
2. Acesse o diretório "hugo_sd_tp" dentro da pasta do projeto clonado
3. Altere o as credênciais do banco de dados no arquivo "settings.py" para as credênciais do seu sevidor PostgreSQL.
4. Execute o comando para executar as migrations:
```sh
$ python manage.py migrate
```
6. Execute o comando para rodar a aplicação:
```sh
$ python manage.py runserver
```
