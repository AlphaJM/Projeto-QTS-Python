import banco_de_dados
import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError


try:
    conectar_banco = psycopg2.connect(**banco_de_dados.informacao_db)
    # Verifique a existência das tabelas
    resultados = banco_de_dados.verificar_existencia_tabelas(conectar_banco, banco_de_dados.tabelas)
    # Verifique se todas as tabelas existem
    todas_existem = all(existe for _, existe in resultados)

    if todas_existem:
        print("Todas as tabelas existem.")
        # Código para executar se todas as tabelas existem
        # ...
    else:
        print("Algumas tabelas não existem:")
        for tabela, existe in resultados:
            if not existe:
                print(f" - {tabela}")
        # Código para executar se alguma tabela não existir
        # ...

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conectar_banco:
        conectar_banco.close()