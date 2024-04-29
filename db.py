import psycopg2

connection = psycopg2.connect(
        dbname="Sistema_QTS",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    
    # Se a conexão for bem-sucedida, imprime uma mensagem
print("Conexão bem-sucedida!")

def consultar_tabela(nome_tabela):
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