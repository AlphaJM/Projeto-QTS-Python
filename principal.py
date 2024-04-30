# Aqui vai ser o arquivo principal do projeto
"""import psycopg2

# Conecta ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="Sistema_QTS"
)"""

#Exemplo de matriz 4x6 pois são 6 dias (segunda à sábado) e são 4 horários de aula por dia



semana_matriz = [[0, 0, 0, 0, 0, 0]
                 [0, 0, 0, 0, 0, 0]
                 [0, 0, 0, 0, 0, 0]
                 [0, 0, 0, 0, 0, 0]]

def buscar_horario_disponivel():
    horario_livre = True
    
    for linha in semana_matriz:
        for elemento in linha:
            if elemento == 0:
                return horario_livre == True
            else:
                return horario_livre == False    
        

 
def cadastrar_curso(nome_curso,tema_curso):
    nome_curso == nome_curso
    tema_curso == tema_curso

def cadastrar_materia(nome_materia, quantidade_horas, curso):
    nome_materia == nome_materia
    quantidade_horas == quantidade_horas
    curso == curso

def cadastrar_professor(nome_professor, idade_professor, sexo):
    nome_professor == nome_professor
    idade_professor == idade_professor
    if sexo == 0:
        sexo == "masculino"
    elif sexo == 1:
        sexo == "feminino"
    else:
        print("Não foi possivel determinar seu sexo!")

    print(nome_professor)
    print(idade_professor)
    print(sexo)

def teste():
    print("Testando")

escolha = int(input("Bem vindo ao sistema de horário, digite o número para a escolha do que fazer: \n1- Cadastrar Professor\n2- Cadastrar Materia\n3- Cadastrar Curso"))

if escolha == 1:
    nome = input("Digite o nome do Professor: ")
    idade = input("Digite a idade do professor: ")
    sexo = input("Digite 0 para Masculino e 1 para feminino\n")
    cadastrar_professor(nome, idade, sexo)
