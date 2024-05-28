# Arquivo para fazer a conexão com o banco de dados, criar e verificar a criação das tabelas de banco de dados  essenciais para o projeto


import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

informacao_conexao_db = {
        #Para chamar as conexões do banco de dados, passar como parametro na função
        'dbname': 'Sistema_QTS',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
    }

tabelas = [
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

def main(informacao_db):
    
    try:
        conectar_banco = psycopg2.connect(**informacao_db)
        # Verifique a existência das tabelas
        resultados = verificar_existencia_tabelas(conectar_banco, tabelas)
        # Verifique se todas as tabelas existem
        todas_existem = all(existe for _, existe in resultados)

        if todas_existem:
            print("Todas as tabelas existem.")
            # Código para executar se todas as tabelas existem
            # ...
        else:
            print("Algumas tabelas não existem:")
            for tabela, existe in resultados:
                if not existe:
                    print(f" - {tabela}")
            # Código para executar se alguma tabela não existir
            # ...

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conectar_banco:
            conectar_banco.close()




def verificar_existencia_tabelas(informacao_db, tabelas):
    conectar_banco = psycopg2.connect(**informacao_db)
    resultados = []
    with conectar_banco.cursor() as cur:
        for tabela in tabelas:
            query = sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)")
            cur.execute(query, (tabela,))
            existe = cur.fetchone()[0]
            resultados.append((tabela, existe))
    print(resultados)
    return resultados



def conectar_banco_de_dados(informacao_db):
    try:
        # Tentando conectar ao banco de dados
        conectar_banco = psycopg2.connect(**informacao_db)
        print("Banco de dados conectado com sucesso!")
        # Retornando a conexão para ser usada posteriormente se necessário
        return conectar_banco
    except (Exception, psycopg2.DatabaseError) as erro:
        # Tratando o erro de conexão e exibindo a mensagem de erro
        print(f"Erro ao conectar ao banco de dados: {erro}")
        # Opcionalmente, pode-se retornar None ou False para indicar falha na conexão
        return None



def criar_tabelas_iniciais(informacao_db):
    
    conectar_banco = psycopg2.connect(**informacao_db)
    print("Banco de dados conectado!")
    cursor = conectar_banco.cursor()

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
        )"""]
    

    try:
        for comando in comandos_criacao_tabelas_essenciais:
            cursor.execute(comando)
        
        conectar_banco.commit()
        print("Tabelas criadas com sucesso.")
    
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar tabelas: {erro}")
        conectar_banco.rollback()
    
    finally:
        
        # fechar o cursor
        cursor.close()

        # Encerrar a conexão com o banco de dados
        conectar_banco.close()



"""print("Testando conexão com banco de dados")
conectar_banco_de_dados(informacao_conexao_db)""" # funciona

"""print("Teste de criação de tabelas")
criar_tabelas_iniciais(informacao_conexao_db)""" #Essa porra funciona caralho

"""verificar_existencia_tabelas(informacao_conexao_db, tabelas)""" # funciona

if __name__ == "__main__":
    main(informacao_conexao_db)