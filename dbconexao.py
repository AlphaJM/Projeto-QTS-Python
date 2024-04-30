import psycopg2

conectar_banco = psycopg2.connect(
        dbname="Sistema_QTS",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    
    # Se a conexão for bem-sucedida, imprime uma mensagem
print("Conexão bem-sucedida!")

# Função para inserir dados
def inserir_dados(nome_tabela, **valores):
    connection = conectar_banco()
    cursor = connection.cursor()

    colunas = ', '.join(valores.keys())
    placeholders = ', '.join(['%s'] * len(valores))
    query = f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({placeholders})"
    cursor.execute(query, list(valores.values()))

    # Commit da transação
    connection.commit()
    # Fecha o cursor
    cursor.close()
    # Fecha a conexão
    connection.close()

# Função para selecionar dados
def selecionar_dados(nome_tabela, *colunas):
    connection = conectar_banco()
    cursor = connection.cursor()

    if colunas:
        colunas = ', '.join(colunas)
    else:
        colunas = '*'

    query = f"SELECT {colunas} FROM {nome_tabela}"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Fecha o cursor
    cursor.close()
    # Fecha a conexão
    connection.close()

    return rows

# Função para atualizar dados
def atualizar_dados(nome_tabela, identificador, **valores):
    connection = conectar_banco()
    cursor = connection.cursor()

    sets = ', '.join([f"{coluna} = %s" for coluna in valores.keys()])
    query = f"UPDATE {nome_tabela} SET {sets} WHERE id = %s"
    cursor.execute(query, list(valores.values()) + [identificador])

    # Commit da transação
    connection.commit()
    # Fecha o cursor
    cursor.close()
    # Fecha a conexão
    connection.close()

# Função para excluir dados
def excluir_dados(nome_tabela, identificador):
    connection = conectar_banco()
    cursor = connection.cursor()

    query = f"DELETE FROM {nome_tabela} WHERE id = %s"
    cursor.execute(query, (identificador,))

    # Commit da transação
    connection.commit()
    # Fecha o cursor
    cursor.close()
    # Fecha a conexão
    connection.close()

"""def show_tabela():
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
    
    cursor.execute(f"INSERT INTO {nome_tabela} (NOME_PROFESSORES, FORMACAO) VALUES ('{value1}', '{value2}')")

    # Commit da transação
    connection.commit()
    # Fecha o cursor
    cursor.close()

    
    
    

show_tabela()
insert_tabela("PROFESSORES", "João", "Sistemas-de-Informação")
#select_tabela("PROFESSORES")
connection.close()"""