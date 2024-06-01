import psycopg2
from psycopg2 import sql
from flask import Blueprint
from app.models.banco_de_dados import conectar_banco_de_dados, informacao_conexao_db

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/cadastro')
def cadastro():
    def cadastrar_titularidade(descricao):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Titularidades (Descricao_Titularidade) VALUES (%s) RETURNING ID_Titularidade", (descricao,))
                id_titularidade = cursor.fetchone()[0]
                conexao.commit()
                print(f"Titularidade cadastrada com sucesso com ID: {id_titularidade}")
                return id_titularidade
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar titularidade: {e}")
        finally:
            conexao.close()

    def cadastrar_professor(nome, especializacao, codigo_lattes, id_titularidade):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Professores (Nome, Especializacao, Codigo_Lattes, ID_Titularidade) VALUES (%s, %s, %s, %s) RETURNING ID_Professor",
                            (nome, especializacao, codigo_lattes, id_titularidade))
                id_professor = cursor.fetchone()[0]
                conexao.commit()
                print(f"Professor cadastrado com sucesso com ID: {id_professor}")
                return id_professor
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar professor: {e}")
        finally:
            conexao.close()

    def cadastrar_area_curso(nome_area_curso):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Area_Curso (Nome_Area_Curso) VALUES (%s) RETURNING ID_Area_Curso", (nome_area_curso,))
                id_area_curso = cursor.fetchone()[0]
                conexao.commit()
                print(f"Área de curso cadastrada com sucesso com ID: {id_area_curso}")
                return id_area_curso
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar área de curso: {e}")
        finally:
            conexao.close()

    def cadastrar_materia(nome_materia, descricao_materia, carga_horaria, id_area_curso):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Materias (Nome_Materia, Descricao_Materia, Carga_Horaria, ID_Area_Curso) VALUES (%s, %s, %s, %s) RETURNING ID_Materia",
                            (nome_materia, descricao_materia, carga_horaria, id_area_curso))
                id_materia = cursor.fetchone()[0]
                conexao.commit()
                print(f"Matéria cadastrada com sucesso com ID: {id_materia}")
                return id_materia
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar matéria: {e}")
        finally:
            conexao.close()

    def cadastrar_curso(nome_curso, descricao_curso):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Cursos (Nome_Curso, Descricao_Curso) VALUES (%s, %s) RETURNING ID_Curso", (nome_curso, descricao_curso))
                id_curso = cursor.fetchone()[0]
                conexao.commit()
                print(f"Curso cadastrado com sucesso com ID: {id_curso}")
                return id_curso
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar curso: {e}")
        finally:
            conexao.close()

    def cadastrar_semestre(nome_semestre):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Semestres (Nome_Semestre) VALUES (%s) RETURNING ID_Semestre", (nome_semestre,))
                id_semestre = cursor.fetchone()[0]
                conexao.commit()
                print(f"Semestre cadastrado com sucesso com ID: {id_semestre}")
                return id_semestre
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar semestre: {e}")
        finally:
            conexao.close()

    def associar_professor_materia(id_professor, id_materia):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Associacao_Professor_Materia (ID_Professor, ID_Materia) VALUES (%s, %s) RETURNING ID_Associacao_Professor_Materia",
                            (id_professor, id_materia))
                id_associacao = cursor.fetchone()[0]
                conexao.commit()
                print(f"Associação de professor e matéria cadastrada com sucesso com ID: {id_associacao}")
                return id_associacao
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao associar professor e matéria: {e}")
        finally:
            conexao.close()

    def associar_materia_curso(id_materia, id_curso, id_semestre):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Associacao_Materia_Curso (ID_Materia, ID_Curso, ID_Semestre) VALUES (%s, %s, %s) RETURNING ID_Associacao_Materia_Curso",
                            (id_materia, id_curso, id_semestre))
                id_associacao = cursor.fetchone()[0]
                conexao.commit()
                print(f"Associação de matéria e curso cadastrada com sucesso com ID: {id_associacao}")
                return id_associacao
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao associar matéria e curso: {e}")
        finally:
            conexao.close()

    def cadastrar_nome_cronograma(descricao):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Nome_Cronograma_Aula (Descricao_Nome_Cronograma_Aula) VALUES (%s) RETURNING ID_Nome_Cronograma_Aula", (descricao,))
                id_cronograma = cursor.fetchone()[0]
                conexao.commit()
                print(f"Nome do cronograma cadastrado com sucesso com ID: {id_cronograma}")
                return id_cronograma
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar nome do cronograma: {e}")
        finally:
            conexao.close()

    def cadastrar_periodo(nome_periodo):
        # Periodo se é noturno, verspertino ou matutino
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Periodos (Nome_Periodo) VALUES (%s) RETURNING ID_Periodo", (nome_periodo,))
                id_periodo = cursor.fetchone()[0]
                conexao.commit()
                print(f"Período cadastrado com sucesso com ID: {id_periodo}")
                return id_periodo
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar período: {e}")
        finally:
            conexao.close()

    def cadastrar_horario_aula(nome_horario, hora_inicio, hora_fim, id_periodo):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Horarios_Aula (Nome_Horario_Aula, Hora_Inicio, Hora_Fim, ID_Periodo) VALUES (%s, %s, %s, %s) RETURNING ID_Horario_Aula",
                            (nome_horario, hora_inicio, hora_fim, id_periodo))
                id_horario = cursor.fetchone()[0]
                conexao.commit()
                print(f"Horário de aula cadastrado com sucesso com ID: {id_horario}")
                return id_horario
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar horário de aula: {e}")
        finally:
            conexao.close()

    def cadastrar_cronograma_aula(nome_cronograma, id_horario_aula, id_nome_cronograma, id_associacao_materia_curso):
        conexao = conectar_banco_de_dados(informacao_conexao_db)
        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO Cronograma_Aula (Nome_Cronograma_Aula, ID_Horario_Aula, ID_Nome_Cronograma_Aula, ID_Associacao_Materia_Curso) VALUES (%s, %s, %s, %s) RETURNING ID_Cronograma_Aula",
                            (nome_cronograma, id_horario_aula, id_nome_cronograma, id_associacao_materia_curso))
                id_cronograma_aula = cursor.fetchone()[0]
                conexao.commit()
                print(f"Cronograma de aula cadastrado com sucesso com ID: {id_cronograma_aula}")
                return id_cronograma_aula
        except Exception as e:
            conexao.rollback()
            print(f"Erro ao cadastrar cronograma de aula: {e}")
        finally:
            conexao.close()

    return "Cadastro"
