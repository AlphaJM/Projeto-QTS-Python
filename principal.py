# Aqui vai ser o arquivo principal do projeto

import dbfunctions
import dbconexao


"""import psycopg2

# Conecta ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="Sistema_QTS"
)"""

#Exemplo de matriz 4x6 pois são 6 dias (segunda à sábado) e são 4 horários de aula por dia


semana_matriz = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

def tem_horario_disponivel():
    contador_horario_livre = 0
    
    for linha in semana_matriz:
        for elemento in linha:
            if elemento == 0:
                contador_horario_livre += 1

    return contador_horario_livre > 0

# Example usage
#print(tem_horario_disponivel())  # This will print True if there's at least one available time slot, otherwise False
  
"""def teste():
    print("Testando")"""

escolha = int(input("Bem vindo ao sistema de horário, digite o número para a escolha do que fazer: \n1- Cadastrar Professor\n2- Cadastrar Materia\n3- Cadastrar Curso"))

if escolha == 1:
    nome = input("Digite o nome do Professor: ")
    formacao = input("Digite a formação do professor: ")
    dbfunctions.cadastrar_professor(nome, formacao)
