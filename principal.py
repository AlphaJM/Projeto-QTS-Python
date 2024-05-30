import banco_de_dados
import psycopg2

def main():
    try:
        # Conectar ao banco de dados
        conectar_banco = banco_de_dados.conectar_banco_de_dados(banco_de_dados.informacao_conexao_db)
        
        if not conectar_banco:
            return

        # Verificar a existência das tabelas
        resultados = banco_de_dados.verificar_existencia_tabelas(banco_de_dados.informacao_conexao_db, banco_de_dados.tabelas)
        
        # Verificar se todas as tabelas existem
        todas_existem = all(existe for _, existe in resultados)

        if todas_existem:
            print("Todas as tabelas existem.")
        else:
            print("Algumas tabelas não existem. Criando tabelas...")
            banco_de_dados.criar_tabelas_iniciais(banco_de_dados.informacao_conexao_db)

        # Importar e executar o script de gerar horário escolar
        import gerar_horario
        gerar_horario.main()

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
    finally:
        if conectar_banco:
            conectar_banco.close()

if __name__ == "__main__":
    main()
