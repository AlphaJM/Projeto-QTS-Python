import dbconexao

def cadastrar_curso(nome_curso,tema_curso):
    nome_curso == nome_curso
    tema_curso == tema_curso

def cadastrar_materia(nome_materia, quantidade_horas, curso):
    nome_materia == nome_materia
    quantidade_horas == quantidade_horas
    curso == curso

def cadastrar_professor(nome_professor, formacao):
    dbconexao.insert_tabela('PROFESSORES', nome_professor, formacao)