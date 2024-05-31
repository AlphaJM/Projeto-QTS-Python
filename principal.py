import banco_de_dados
import cadastro
import psycopg2
import gerar_horario

def exibir_menu_admin():
    print("------ Menu Admin ------")
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
    print("2. Entrar no Menu de Administrador")
    print("0. Sair")

def main():
    try:
        # Conectar ao banco de dados
        #conexao_banco = banco_de_dados.verificacao_para_conexao_db()
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
                opcao = input("Escolha uma opção: ")

                if opcao in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'}:
                    
                    if opcao == '1':
                        titularidade = input('Digite o nome da titularidade: ')
                        cadastro.cadastrar_titularidade(titularidade)
                    
                    elif opcao == '2':
                        mapa_titularidades = {
                            '1': 7,
                            '2': 8,
                            '3': 9,
                            '4': 10,
                            '5': 12,
                            '6': 11
                        }
                        nome = input('Digite o nome do Professor(a): ')
                        especializacao = input('Digite a especialização do Professor(a): ')
                        codigo_lattes = int(input('Digite o Código Lattes do Professor(a): '))
                        prof_titularidade = input('Digite o número referente ao nível de titularidade do Professor(a):\n1- Graduado;\n2- Especialista;\n3- Mestre;\n4- Doutor;\n5- Pós-Doutor;\n6- Livre-Docênte\nEscolha: ')
                        
                        if prof_titularidade in mapa_titularidades:
                            cadastro.cadastrar_professor(nome, especializacao, codigo_lattes, mapa_titularidades[prof_titularidade])
                        else:
                            print('Escolha Inválida!')

                    elif opcao == '3':
                        nome_area_curso = str(input('Digite a área do curso: '))
                        cadastro.cadastrar_area_curso(nome_area_curso)

                    elif opcao == '4':
                        nome_materia = str(input('Digite o nome da matéria: '))
                        descricao_materia = str(input('Fale sobre a matéria: '))
                        carga_horaria = int(input('Digite a carga horária da matéria: '))
                        area_curso = int(input('Escolha a area do curso:\n1- tecnologia\nEscolha: '))
                        if area_curso == 1:
                            area_curso == 1
                            cadastro.cadastrar_materia(nome_materia, descricao_materia, carga_horaria, area_curso)
                        else:
                            print('Escolha invalida!')
                        

                    elif opcao == '5':
                        nome_curso = input('Digite o nome do curso: ')
                        descricao_curso = input('Descreva sobre o curso: ')
                        cadastro.cadastrar_curso(nome_curso, descricao_curso)
                
                    elif opcao == '6':
                        semestre = str(input('Digite qual semestre deseja cadastrar: '))
                        cadastro.cadastrar_semestre(semestre)

                    elif opcao == '7':
                        id_professor = input('Digite o ID do professor: ')
                        id_materia = input('Digite o ID da matéria: ')
                        cadastro.associar_professor_materia(id_professor, id_materia)

                    elif opcao == '8':
                        id_materia = input('Digite o ID da matéria: ')
                        id_curso = input('Digite o ID do curso: ')
                        id_semestre = input('Digite o ID do semestre: ')
                        cadastro.associar_materia_curso(id_materia, id_curso, id_semestre)

                    elif opcao == '9':
                        cronograma = str(input('Digite o nome do cronograma que deseja cadastrar: '))
                        cadastro.cadastrar_nome_cronograma(cronograma)

                    elif opcao == '10':
                        nome_cronograma = input('Digite o nome do cronograma de aula: ')
                        id_horario_aula = input('Digite o ID do horário de aula: ')
                        id_nome_cronograma = input('Digite o ID do nome do cronograma: ')
                        id_associacao_materia_curso = input('Digite o ID da associação matéria-curso: ')
                        cadastro.cadastrar_cronograma_aula(nome_cronograma, id_horario_aula, id_nome_cronograma, id_associacao_materia_curso)

                    elif opcao == '11':
                        periodo = str(input('Digite o periodo que deseja cadastrar: '))
                        cadastro.cadastrar_periodo(periodo)

                    else:
                        mapa_periodo_horario = {
                            '1': 1,
                            '2': 2,
                            '3': 3
                        }
                        nome_horario = str(input('Digite o nome do horário: '))
                        hora_inicio = input('Digite a hora de inicio do horário (Formato necessário HH:MM:SS): ')
                        hora_fim = input('Digite a hora que finaliza o horário (HH:MM:SS): ')
                        periodo_horario = int(input('Escolha o periodo que o horario será criado:\n1- Matutino\n2- Vespertino\n3- Noturno\nEscolha: '))
                        if periodo_horario in mapa_periodo_horario:
                            cadastro.cadastrar_horario_aula(nome_horario, hora_inicio, hora_fim, mapa_periodo_horario[periodo_horario])
                        else:
                            print('Opção Invalida!')

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
    finally:
        if conexao_banco:
            conexao_banco.close()

if __name__ == "__main__":
    main()
