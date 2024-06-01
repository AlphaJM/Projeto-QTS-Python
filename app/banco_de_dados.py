import psycopg2
from psycopg2 import sql

# Configuração padrão para a conexão com o banco de dados
informacao_conexao_db = {
    'dbname': 'Sistema_QTS',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
}

TABELAS = [
    'titularidades',
    'professores',
    'area_curso',
    'materias',
    'cursos',
    'semestres',
    'associacao_professor_materia',
    'associacao_materia_curso',
    'nome_cronograma_aula',
    'periodos',
    'horarios_aula',
    'cronograma_aula'
]

def verificacao_para_conexao_db():
    print('Para realizar a conexão com o banco de dados PostGres digite as informações necessárias')
    dbname = input('Digite o nome do Banco de dados: ')
    user = input('Digite o nome de usuário: ')
    password = input('Digite a senha: ')
    host = input('Digite o Host: ')

    return {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
    }

def executar_query(conexao, query, values=None):
    try:
        with conexao.cursor() as cursor:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            if cursor.description:
                return cursor.fetchone()[0]
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao executar query: {e}")
    return None

def verificar_existencia_tabelas(conexao, tabelas):
    resultados = []
    for tabela in tabelas:
        query = sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)")
        existe = executar_query(conexao, query, (tabela,))
        resultados.append((tabela, existe))
    return resultados

def conectar_banco_de_dados(informacao_db):
    try:
        conexao = psycopg2.connect(**informacao_db)
        print("Banco de dados conectado com sucesso!")
        return conexao
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def criar_tabelas_iniciais(conexao):
    comandos_criacao_tabelas_essenciais = [
        """CREATE TABLE Titularidades (
        ID_Titularidade SERIAL PRIMARY KEY,
        Descricao_Titularidade VARCHAR NOT NULL
        )""",
        """CREATE TABLE Professores (
            ID_Professor SERIAL PRIMARY KEY,
            Nome VARCHAR NOT NULL,
            Especializacao VARCHAR,
            Codigo_Lattes INTEGER,
            ID_Titularidade INTEGER,
            FOREIGN KEY (ID_Titularidade) REFERENCES Titularidades(ID_Titularidade)
        )""",
        """CREATE TABLE Area_Curso (
            ID_Area_Curso SERIAL PRIMARY KEY,
            Nome_Area_Curso VARCHAR NOT NULL
        )""",
        """CREATE TABLE Materias (
            ID_Materia SERIAL PRIMARY KEY,
            Nome_Materia VARCHAR NOT NULL,
            Descricao_Materia VARCHAR,
            Carga_Horaria INTEGER,
            ID_Area_Curso INTEGER,
            FOREIGN KEY (ID_Area_Curso) REFERENCES Area_Curso(ID_Area_Curso)
        )""",
        """CREATE TABLE Cursos (
            ID_Curso SERIAL PRIMARY KEY,
            Nome_Curso VARCHAR NOT NULL,
            Descricao_Curso VARCHAR
        )""",
        """CREATE TABLE Semestres (
            ID_Semestre SERIAL PRIMARY KEY,
            Nome_Semestre VARCHAR NOT NULL
        )""",
        """CREATE TABLE Associacao_Professor_Materia (
            ID_Associacao_Professor_Materia SERIAL PRIMARY KEY,
            ID_Professor INTEGER,
            ID_Materia INTEGER,
            FOREIGN KEY (ID_Professor) REFERENCES Professores(ID_Professor),
            FOREIGN KEY (ID_Materia) REFERENCES Materias(ID_Materia)
        )""",
        """CREATE TABLE Associacao_Materia_Curso (
            ID_Associacao_Materia_Curso SERIAL PRIMARY KEY,
            ID_Materia INTEGER,
            ID_Curso INTEGER,
            ID_Semestre INTEGER,
            FOREIGN KEY (ID_Materia) REFERENCES Materias(ID_Materia),
            FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_Curso),
            FOREIGN KEY (ID_Semestre) REFERENCES Semestres(ID_Semestre)
        )""",
        """CREATE TABLE Nome_Cronograma_Aula (
            ID_Nome_Cronograma_Aula SERIAL PRIMARY KEY,
            Descricao_Nome_Cronograma_Aula VARCHAR NOT NULL
        )""",
        """CREATE TABLE Periodos (
            ID_Periodo SERIAL PRIMARY KEY,
            Nome_Periodo VARCHAR NOT NULL
        )""",
        """CREATE TABLE Horarios_Aula (
            ID_Horario_Aula SERIAL PRIMARY KEY,
            Nome_Horario_Aula VARCHAR NOT NULL,
            Hora_Inicio TIME,
            Hora_Fim TIME,
            ID_Periodo INTEGER,
            FOREIGN KEY (ID_Periodo) REFERENCES Periodos(ID_Periodo)
        )""",
        """CREATE TABLE Cronograma_Aula (
            ID_Cronograma_Aula SERIAL PRIMARY KEY,
            Nome_Cronograma_Aula VARCHAR NOT NULL,
            ID_Horario_Aula INTEGER,
            ID_Nome_Cronograma_Aula INTEGER,
            ID_Associacao_Materia_Curso INTEGER,
            FOREIGN KEY (ID_Horario_Aula) REFERENCES Horarios_Aula(ID_Horario_Aula),
            FOREIGN KEY (ID_Nome_Cronograma_Aula) REFERENCES Nome_Cronograma_Aula(ID_Nome_Cronograma_Aula),
            FOREIGN KEY (ID_Associacao_Materia_Curso) REFERENCES Associacao_Materia_Curso(ID_Associacao_Materia_Curso)
        )"""
    ]
    try:
        cursor = conexao.cursor()
        for comando in comandos_criacao_tabelas_essenciais:
            cursor.execute(comando)
        conexao.commit()
        print("Tabelas criadas com sucesso.")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar tabelas: {erro}")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
