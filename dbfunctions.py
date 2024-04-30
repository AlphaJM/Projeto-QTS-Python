import dbconexao

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