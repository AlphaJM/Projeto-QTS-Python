import banco_de_dados
import psycopg2
import gerar_horario

def exibir_menu():
    print("------ Menu ------")
    print("1. Cadastrar Titularidade")
    print("2. Cadastrar Professor")
    print("3. Cadastrar Área de Curso")
    print("4. Cadastrar Matéria")
    print("5. Cadastrar Curso")
    print("6. Cadastrar Semestre")
    print("7. Associar Professor a Matéria")
    print("8. Associar Matéria a Curso")
    print("9. Cadastrar Nome de Cronograma de Aula")
    print("10. Cadastrar Período")
    print("11. Cadastrar Horário de Aula")
    print("12. Cadastrar Cronograma de Aula")
    print("13. Gerar Horário Escolar")
    print("0. Sair")

def main():
    try:
        # Conectar ao banco de dados
        conexao_banco = banco_de_dados.conectar_banco_de_dados(banco_de_dados.informacao_conexao_db)
        
        if not conexao_banco:
            return

        # Verificar a existência das tabelas
        resultados = banco_de_dados.verificar_existencia_tabelas(conexao_banco, banco_de_dados.TABELAS)
        
        # Verificar se todas as tabelas existem
        todas_existem = all(existe for _, existe in resultados)

        if todas_existem:
            print("Todas as tabelas existem.")
        else:
            print("Algumas tabelas não existem. Criando tabelas...")
            banco_de_dados.criar_tabelas_iniciais(conexao_banco)

        while True:
            exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == '0':
                break
            elif opcao == '13':
                gerar_horario.main()
            elif opcao in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'}:
                # Aqui você pode chamar a função correspondente ao número da opção selecionada
                pass
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
    finally:
        if conexao_banco:
            conexao_banco.close()

if __name__ == "__main__":
    main()
