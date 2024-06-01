import app.models.banco_de_dados as banco_de_dados
from app.routes import gerar_horario, cadastro
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def exibir_menu_admin():
    print("------ Admin - Menu de Cadastro ------")
    print("1. Cadastrar Titularidade")
    print("2. Cadastrar Professor")
    print("3. Cadastrar Área de Curso")
    print("4. Cadastrar Matéria")
    print("5. Cadastrar Curso")
    print("6. Cadastrar Semestre")
    print("7. Associar Professor a Matéria")
    print("8. Associar Matéria a Curso")
    print("9. Cadastrar o nome de Cronograma de Aula")
    print("10. Cadastrar o Cronograma de Aula")
    print("11. Cadastrar Período")
    print("12. Cadastrar Horário de Aula")
    print("0. Sair")

def exibir_menu():
    print("------ Menu ------")
    print("1. Gerar Horário Escolar")
    print("2. Administrador")
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
        
            elif opcao == '1':
                gerar_horario.main()

            elif opcao == '2':
                exibir_menu_admin()
                opcao_admin = input("Escolha uma opção: ")

                if opcao_admin == '0':
                    continue

                elif opcao_admin == '1':
                    titularidade = input('Digite o nome da titularidade: ')
                    cadastro.cadastrar_titularidade(titularidade)
                
                elif opcao_admin == '2':
                    nome = input('Digite o nome do Professor(a): ')
                    especializacao = input('Digite a especialização do Professor(a): ')
                    codigo_lattes = int(input('Digite o Código Lattes do Professor(a): '))
                    id_titularidade = int(input('Digite o ID da Titularidade do Professor(a): '))
                    cadastro.cadastrar_professor(nome, especializacao, codigo_lattes, id_titularidade)

                elif opcao_admin == '3':
                    nome_area_curso = input('Digite a área do curso: ')
                    cadastro.cadastrar_area_curso(nome_area_curso)

                elif opcao_admin == '4':
                    nome_materia = input('Digite o nome da matéria: ')
                    descricao_materia = input('Fale sobre a matéria: ')
                    carga_horaria = int(input('Digite a carga horária da matéria: '))
                    id_area_curso = int(input('Digite o ID da Area do Curso relacionado a matéria: '))
                    cadastro.cadastrar_materia(nome_materia, descricao_materia, carga_horaria, id_area_curso)
                
                elif opcao_admin == '5':
                    nome_curso = input('Digite o nome do curso: ')
                    descricao_curso = input('Descreva sobre o curso: ')
                    cadastro.cadastrar_curso(nome_curso, descricao_curso)
            
                elif opcao_admin == '6':
                    semestre = input('Digite qual semestre deseja cadastrar: ')
                    cadastro.cadastrar_semestre(semestre)

                elif opcao_admin == '7':
                    id_professor = input('Digite o ID do professor: ')
                    id_materia = input('Digite o ID da matéria: ')
                    cadastro.associar_professor_materia(id_professor, id_materia)

                elif opcao_admin == '8':
                    id_materia = input('Digite o ID da matéria: ')
                    id_curso = input('Digite o ID do curso: ')
                    id_semestre = input('Digite o ID do semestre: ')
                    cadastro.associar_materia_curso(id_materia, id_curso, id_semestre)

                elif opcao_admin == '9':
                    cronograma = input('Digite o nome do cronograma que deseja cadastrar: ')
                    cadastro.cadastrar_nome_cronograma(cronograma)

                elif opcao_admin == '10':
                    nome_cronograma = input('Digite o nome do cronograma de aula: ')
                    id_horario_aula = input('Digite o ID do horário de aula: ')
                    id_nome_cronograma = input('Digite o ID do nome do cronograma: ')
                    id_associacao_materia_curso = input('Digite o ID da associação matéria-curso: ')
                    cadastro.cadastrar_cronograma_aula(nome_cronograma, id_horario_aula, id_nome_cronograma, id_associacao_materia_curso)

                elif opcao_admin == '11':
                    periodo = input('Digite o periodo que deseja cadastrar: ')
                    cadastro.cadastrar_periodo(periodo)

                elif opcao_admin == '12':
                    nome_horario = input('Digite o nome do horário: ')
                    hora_inicio = input('Digite a hora de inicio do horário (Formato necessário HH:MM:SS): ')
                    hora_fim = input('Digite a hora que finaliza o horário (HH:MM:SS): ')
                    id_periodo = int(input('Digite o ID do Periodo relacionado ao Horário da aula: '))
                    cadastro.cadastrar_horario_aula(nome_horario, hora_inicio, hora_fim, id_periodo)

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
    finally:
        if 'conexao_banco' in locals() and conexao_banco:
            conexao_banco.close()

if __name__ == "__main__":
    main()
