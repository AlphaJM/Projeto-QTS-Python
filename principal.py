import banco_de_dados
import psycopg2
import gerar_horario

def main():
    try:
        conexao = banco_de_dados.conectar_banco_de_dados(banco_de_dados.informacao_conexao_db)
        if not conexao:
            return

        resultados = banco_de_dados.verificar_existencia_tabelas(conexao, banco_de_dados.TABELAS)
        todas_existem = all(existe for _, existe in resultados)

        if todas_existem:
            print("Todas as tabelas existem.")
        else:
            print("Algumas tabelas não existem. Criando tabelas...")
            banco_de_dados.criar_tabelas_iniciais(conexao)

        gerar_horario.main()

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    main()
