# Aqui vai ser o arquivo principal do projeto

def cadastrar_pessoas(nome_pessoa,idade,sexo,e_professor):
    nome_pessoa == nome_pessoa
    idade == idade
    if sexo == 0:
        sexo == "masculino"
    elif sexo == 1:
        sexo == "feminino"
    else:
        print("Não foi possivel determinar seu sexo!")
    e_professor = e_professor


"""
# Exemplo de conexão para banco de dados
# É preciso baixar essa biblioteca de conexão com postgress: pip install psycopg2

import psycopg2

# Conecta ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Cria um cursor para executar consultas
cursor = conn.cursor()

# Executa uma consulta SELECT
cursor.execute("SELECT * FROM sua_tabela")

# Recupera os resultados da consulta
resultados = cursor.fetchall()

# Imprime os resultados
for linha in resultados:
    print(linha)

# Fecha o cursor e a conexão
cursor.close()
conn.close()

"""