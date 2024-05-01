import dbconexao

def cadastrar_curso(nome_curso,tema_curso):
    dbconexao.insert_db('CURSO', nome_curso, tema_curso)

def cadastrar_materia(nome_materia, quantidade_horas, curso):
    dbconexao.insert_db('MATERIAS',nome_materia, quantidade_horas, curso)

def cadastrar_professor(nome_professor, formacao):
    dbconexao.insert_db('PROFESSORES', nome_professor, formacao)