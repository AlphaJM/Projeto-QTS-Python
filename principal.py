# Aqui vai ser o arquivo principal do projeto
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

escolha = int(input("Bem vindo ao sistema de horário, digite o número para a escolha do que fazer: \n1- Cadastrar Professor\n2- Cadastrar Materia\n3- Cadastrar Curso"))

if escolha == 1:
    nome = input("Digite o nome do Professor: ")
    idade = input("Digite a idade do professor: ")
    sexo = input("Digite 0 para Masculino e 1 para feminino\n")
    cadastrar_professor(nome, idade, sexo)




"""
# Exemplo de conexão para banco de dados
# É preciso baixar essa biblioteca de conexão com postgress: pip install psycopg2

import psycopg2

# Conecta ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Cria um cursor para executar consultas
cursor = conn.cursor()

# Executa uma consulta SELECT
cursor.execute("SELECT * FROM sua_tabela")

# Recupera os resultados da consulta
resultados = cursor.fetchall()

# Imprime os resultados
for linha in resultados:
    print(linha)

# Fecha o cursor e a conexão
cursor.close()
conn.close()

"""