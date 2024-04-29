import psycopg2

connection = psycopg2.connect(
        dbname="Sistema_QTS",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    
    # Se a conexão for bem-sucedida, imprime uma mensagem
print("Conexão bem-sucedida!")

def show_tabela():
    cursor = connection.cursor()

    # Executa a consulta SELECT
    cursor.execute("SELECT table_name\nFROM information_schema.tables\nWHERE table_schema = 'public'\nAND table_type = 'BASE TABLE';")

    # Recupera os resultados da consulta
    rows = cursor.fetchall()

    # Itera sobre os resultados e os imprime
    for row in rows:
        print(row)

    # Fecha o cursor e a conexão
    #cursor.close()
    #connection.close()


def select_tabela(nome_tabela):
    cursor = connection.cursor()

    # Executa a consulta SELECT
    cursor.execute(f'SELECT * FROM {nome_tabela}')

    # Recupera os resultados da consulta
    rows = cursor.fetchall()

    # Itera sobre os resultados e os imprime
    for row in rows:
        print(row)

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()

def insert_tabela(nome_tabela, value1, value2):
    cursor = connection.cursor()
    
    cursor.execute(f'INSERT INTO {nome_tabela} (NOME_PROFESSORES, FORMACAO)\nVALUES ({value1}, {value2});')

    # Recupera os resultados da consulta
    rows = cursor.fetchall()

    # Itera sobre os resultados e os imprime
    for row in rows:
        print(row)

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()
    
    
    

show_tabela()
insert_tabela("PROFESSORES", "João", "Sistemas-de-Informação")
#select_tabela("PROFESSORES")