import psycopg2
from banco_de_dados import conectar_banco_de_dados, informacao_conexao_db
import random

Dias_Semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
Numero_Horarios_por_Dia = 4

def buscar_aulas(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT ID_Materia, Nome_Materia FROM Materias")
        return cursor.fetchall()

def horario_valido(horario):
    for dia in horario:
        if len(set(dia)) != len(dia):
            return False
    return True

def gerar_horario(horario, dia_atual, aulas_disponiveis):
    if dia_atual == len(Dias_Semana):
        return horario_valido(horario)

    for combinacao in random.sample(aulas_disponiveis, Numero_Horarios_por_Dia):
        horario[dia_atual] = combinacao
        novas_aulas_disponiveis = [aula for aula in aulas_disponiveis if aula not in combinacao]

        if gerar_horario(horario, dia_atual + 1, novas_aulas_disponiveis):
            return True

    return False

def gerar_horario_escolar(conexao):
    aulas = buscar_aulas(conexao)
    aulas_ids = [aula[0] for aula in aulas]
    horario_escolar = [[] for _ in Dias_Semana]

    if gerar_horario(horario_escolar, 0, aulas_ids):
        horario_final = []
        for dia, aulas_ids in enumerate(horario_escolar):
            dia_horario = {'dia': Dias_Semana[dia], 'aulas': []}
            for aula_id in aulas_ids:
                for aula in aulas:
                    if aula[0] == aula_id:
                        dia_horario['aulas'].append({'id': aula_id, 'nome': aula[1]})
            horario_final.append(dia_horario)
        return horario_final
    else:
        return None

