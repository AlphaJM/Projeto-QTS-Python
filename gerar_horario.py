import psycopg2
from psycopg2 import sql
import random
from banco_de_dados import conectar_banco_de_dados, informacao_conexao_db

def buscar_aulas(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT ID_Materia, Nome_Materia FROM Materias")
        return cursor.fetchall()

# Configuração do horário escolar
dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
numero_horarios_por_dia = 4

# Função para verificar se o horário é válido
def horario_valido(horario):
    # Verificar se todas as aulas são únicas em cada dia
    for dia in horario:
        if len(set(dia)) != len(dia):
            return False
    return True

# Função de backtracking para gerar o horário
def gerar_horario(horario, dia_atual, aulas_disponiveis):
    if dia_atual == len(dias_semana):
        return horario_valido(horario)
    
    for combinacao in random.sample(aulas_disponiveis, numero_horarios_por_dia):
        horario[dia_atual] = combinacao
        novas_aulas_disponiveis = [aula for aula in aulas_disponiveis if aula not in combinacao]
        
        if gerar_horario(horario, dia_atual + 1, novas_aulas_disponiveis):
            return True
    
    return False

def main():
    # Conectar ao banco de dados
    conexao = conectar_banco_de_dados(informacao_conexao_db)
    if not conexao:
        return
    
    # Buscar aulas do banco de dados
    aulas = buscar_aulas(conexao)
    aulas_ids = [aula[0] for aula in aulas]

    # Inicializando o horário
    horario_escolar = [[] for _ in dias_semana]

    # Gerar o horário usando backtracking
    if gerar_horario(horario_escolar, 0, aulas_ids):
        # Exibindo o horário escolar
        for dia, aulas_ids in enumerate(horario_escolar):
            print(f"\n{dias_semana[dia]}:")
            for aula_id in aulas_ids:
                for aula in aulas:
                    if aula[0] == aula_id:
                        print(f"  Aula ID: {aula_id}, Nome: {aula[1]}")
    else:
        print("Não foi possível gerar um horário sem conflitos.")

    # Fechar a conexão com o banco de dados
    conexao.close()

if __name__ == "__main__":
    main()
