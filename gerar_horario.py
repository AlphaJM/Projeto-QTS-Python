import psycopg2
from banco_de_dados import conectar_banco_de_dados, informacao_conexao_db
import random

def buscar_aulas(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT ID_Materia, Nome_Materia FROM Materias")
        return cursor.fetchall()

Dias_Semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
Numero_Horarios_por_Dia = 4

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

def main():
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    if not conexao:
        return
    
    aulas = buscar_aulas(conexao)
    aulas_ids = [aula[0] for aula in aulas]
    horario_escolar = [[] for _ in Dias_Semana]

    if gerar_horario(horario_escolar, 0, aulas_ids):
        for dia, aulas_ids in enumerate(horario_escolar):
            print(f"\n{Dias_Semana[dia]}:")
            for aula_id in aulas_ids:
                for aula in aulas:
                    if aula[0] == aula_id:
                        print(f"  Aula ID: {aula_id}, Nome: {aula[1]}")
    else:
        print("Não foi possível gerar um horário sem conflitos.")

    conexao.close()

if __name__ == "__main__":
    main()
