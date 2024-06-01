import psycopg2
from banco_de_dados import conectar_banco_de_dados, informacao_conexao_db

dias_da_semana = [
    'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'
]

horario_aulas = {dia: [1, 2, 3, 4] for dia in dias_da_semana}


def gerar_horario():
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    try:
        with conexao.cursor() as cursor:
            dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado"]

            # Criando um dicionário onde cada dia da semana tem uma lista de 4 horários de aula inicializados com None
            horarios_de_aula = {dia: [None, None, None, None] for dia in dias_da_semana}

            # Função para adicionar uma aula aos horários
            def adicionar_aula(aula):
                for dia in dias_da_semana:
                    if aula['carga_horaria'] == 80:
                        if all(slot is None for slot in horarios_de_aula[dia]):
                            horarios_de_aula[dia] = [aula for _ in range(4)]
                            return
                    elif aula['carga_horaria'] == 40:
                        empty_slots = [i for i, slot in enumerate(horarios_de_aula[dia]) if slot is None]
                        if len(empty_slots) >= 2:
                            horarios_de_aula[dia][empty_slots[0]] = aula
                            horarios_de_aula[dia][empty_slots[1]] = aula
                            return

            # Consultando o banco de dados para obter as aulas
            cursor.execute("SELECT nome_materia, carga_horaria FROM materias")
            aulas = cursor.fetchall()

            # Convertendo os resultados da consulta em dicionários de aulas
            aulas = [{'nome': nome_materia, 'carga_horaria': carga_horaria} for nome_materia, carga_horaria in aulas]

            # Loop para adicionar todas as aulas aos horários
            while aulas:
                aula = aulas.pop(0)
                adicionar_aula(aula)

            # Exibindo a estrutura
            for dia, horarios in horarios_de_aula.items():
                print(f"{dia.capitalize()}: {horarios}")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao gerar horário {e}")
    finally:
        conexao.close()

def consulta_materias():
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT nome_materia, carga_horaria FROM materias")
            materias = cursor.fetchall()
            conexao.commit()
            print(f"As matérias existentes são: {materias}")
            return materias
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao buscar materias {e}")
    finally:
        conexao.close()

def consulta_professores():
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT nome FROM professores")
            professores = cursor.fetchall()
            conexao.commit()
            print(f"Os professores cadastrados são: {professores}")
            return professores
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao buscar professores {e}")
    finally:
        conexao.close()

def consulta_cursos():
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT nome_curso FROM cursos")
            cursos = cursor.fetchall()
            conexao.commit()
            print(f"Os cursos cadastrados são: {cursos}")
            return cursos
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao buscar cursos {e}")
    finally:
        conexao.close()


gerar_horario()

"""consulta_materias()
consulta_professores()
consulta_cursos()"""