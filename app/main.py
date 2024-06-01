import tkinter as tk
from tkinter import messagebox
import menu  
import gerar_horario
import cadastro
import banco_de_dados

def chamar_funcao(func):
    def wrapper():
        func()
    return wrapper

def chamar_cadastrar_titularidade():
    def submit():
        titularidade = entry_titularidade.get()
        cadastro.cadastrar_titularidade(titularidade)
        messagebox.showinfo("Sucesso", "Titularidade cadastrada com sucesso!")
        janela_titularidade.destroy()
    
    janela_titularidade = tk.Toplevel(root)
    janela_titularidade.title("Cadastrar Titularidade")
    janela_titularidade.geometry("300x200")
    
    tk.Label(janela_titularidade, text="Digite o nome da titularidade:").pack(pady=10)
    entry_titularidade = tk.Entry(janela_titularidade)
    entry_titularidade.pack(pady=10)
    
    tk.Button(janela_titularidade, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_professor():
    def submit():
        nome = entry_nome.get()
        especializacao = entry_especializacao.get()
        codigo_lattes = int(entry_codigo_lattes.get())
        id_titularidade = int(entry_id_titularidade.get())
        cadastro.cadastrar_professor(nome, especializacao, codigo_lattes, id_titularidade)
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        janela_professor.destroy()

    janela_professor = tk.Toplevel(root)
    janela_professor.title("Cadastrar Professor")
    janela_professor.geometry("400x400")

    tk.Label(janela_professor, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela_professor)
    entry_nome.pack(pady=5)

    tk.Label(janela_professor, text="Especialização:").pack(pady=5)
    entry_especializacao = tk.Entry(janela_professor)
    entry_especializacao.pack(pady=5)

    tk.Label(janela_professor, text="Código Lattes:").pack(pady=5)
    entry_codigo_lattes = tk.Entry(janela_professor)
    entry_codigo_lattes.pack(pady=5)

    tk.Label(janela_professor, text="ID Titularidade:").pack(pady=5)
    entry_id_titularidade = tk.Entry(janela_professor)
    entry_id_titularidade.pack(pady=5)

    tk.Button(janela_professor, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_area_curso():
    def submit():
        nome_area_curso = entry_nome_area_curso.get()
        cadastro.cadastrar_area_curso(nome_area_curso)
        messagebox.showinfo("Sucesso", "Área de curso cadastrada com sucesso!")
        janela_area_curso.destroy()
    
    janela_area_curso = tk.Toplevel(root)
    janela_area_curso.title("Cadastrar Área de Curso")
    janela_area_curso.geometry("300x200")
    
    tk.Label(janela_area_curso, text="Digite a área do curso:").pack(pady=10)
    entry_nome_area_curso = tk.Entry(janela_area_curso)
    entry_nome_area_curso.pack(pady=10)
    
    tk.Button(janela_area_curso, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_materia():
    def submit():
        nome_materia = entry_nome_materia.get()
        descricao_materia = entry_descricao_materia.get()
        carga_horaria = int(entry_carga_horaria.get())
        id_area_curso = int(entry_id_area_curso.get())
        cadastro.cadastrar_materia(nome_materia, descricao_materia, carga_horaria, id_area_curso)
        messagebox.showinfo("Sucesso", "Matéria cadastrada com sucesso!")
        janela_materia.destroy()
    
    janela_materia = tk.Toplevel(root)
    janela_materia.title("Cadastrar Matéria")
    janela_materia.geometry("300x400")

    tk.Label(janela_materia, text="Nome da Matéria:").pack(pady=5)
    entry_nome_materia = tk.Entry(janela_materia)
    entry_nome_materia.pack(pady=5)

    tk.Label(janela_materia, text="Descrição da Matéria:").pack(pady=5)
    entry_descricao_materia = tk.Entry(janela_materia)
    entry_descricao_materia.pack(pady=5)

    tk.Label(janela_materia, text="Carga Horária:").pack(pady=5)
    entry_carga_horaria = tk.Entry(janela_materia)
    entry_carga_horaria.pack(pady=5)

    tk.Label(janela_materia, text="ID da Área do Curso:").pack(pady=5)
    entry_id_area_curso = tk.Entry(janela_materia)
    entry_id_area_curso.pack(pady=5)

    tk.Button(janela_materia, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_curso():
    def submit():
        nome_curso = entry_nome_curso.get()
        descricao_curso = entry_descricao_curso.get()
        cadastro.cadastrar_curso(nome_curso, descricao_curso)
        messagebox.showinfo("Sucesso", "Curso cadastrado com sucesso!")
        janela_curso.destroy()
    
    janela_curso = tk.Toplevel(root)
    janela_curso.title("Cadastrar Curso")
    janela_curso.geometry("300x300")

    tk.Label(janela_curso, text="Nome do Curso:").pack(pady=5)
    entry_nome_curso = tk.Entry(janela_curso)
    entry_nome_curso.pack(pady=5)

    tk.Label(janela_curso, text="Descrição do Curso:").pack(pady=5)
    entry_descricao_curso = tk.Entry(janela_curso)
    entry_descricao_curso.pack(pady=5)

    tk.Button(janela_curso, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_semestre():
    def submit():
        semestre = entry_semestre.get()
        cadastro.cadastrar_semestre(semestre)
        messagebox.showinfo("Sucesso", "Semestre cadastrado com sucesso!")
        janela_semestre.destroy()
    
    janela_semestre = tk.Toplevel(root)
    janela_semestre.title("Cadastrar Semestre")
    janela_semestre.geometry("300x200")

    tk.Label(janela_semestre, text="Digite o semestre:").pack(pady=10)
    entry_semestre = tk.Entry(janela_semestre)
    entry_semestre.pack(pady=10)

    tk.Button(janela_semestre, text="Cadastrar", command=submit).pack(pady=10)

def chamar_associar_professor_materia():
    def submit():
        id_professor = entry_id_professor.get()
        id_materia = entry_id_materia.get()
        cadastro.associar_professor_materia(id_professor, id_materia)
        messagebox.showinfo("Sucesso", "Professor associado à matéria com sucesso!")
        janela_professor_materia.destroy()
    
    janela_professor_materia = tk.Toplevel(root)
    janela_professor_materia.title("Associar Professor a Matéria")
    janela_professor_materia.geometry("300x200")

    tk.Label(janela_professor_materia, text="ID do Professor:").pack(pady=5)
    entry_id_professor = tk.Entry(janela_professor_materia)
    entry_id_professor.pack(pady=5)

    tk.Label(janela_professor_materia, text="ID da Matéria:").pack(pady=5)
    entry_id_materia = tk.Entry(janela_professor_materia)
    entry_id_materia.pack(pady=5)

    tk.Button(janela_professor_materia, text="Associar", command=submit).pack(pady=10)

def chamar_associar_materia_curso():
    def submit():
        id_materia = entry_id_materia.get()
        id_curso = entry_id_curso.get()
        id_semestre = entry_id_semestre.get()
        cadastro.associar_materia_curso(id_materia, id_curso, id_semestre)
        messagebox.showinfo("Sucesso", "Matéria associada ao curso com sucesso!")
        janela_materia_curso.destroy()
    
    janela_materia_curso = tk.Toplevel(root)
    janela_materia_curso.title("Associar Matéria a Curso")
    janela_materia_curso.geometry("300x300")

    tk.Label(janela_materia_curso, text="ID da Matéria:").pack(pady=5)
    entry_id_materia = tk.Entry(janela_materia_curso)
    entry_id_materia.pack(pady=5)

    tk.Label(janela_materia_curso, text="ID do Curso:").pack(pady=5)
    entry_id_curso = tk.Entry(janela_materia_curso)
    entry_id_curso.pack(pady=5)

    tk.Label(janela_materia_curso, text="ID do Semestre:").pack(pady=5)
    entry_id_semestre = tk.Entry(janela_materia_curso)
    entry_id_semestre.pack(pady=5)

    tk.Button(janela_materia_curso, text="Associar", command=submit).pack(pady=10)

def chamar_cadastrar_nome_cronograma():
    def submit():
        cronograma = entry_cronograma.get()
        cadastro.cadastrar_nome_cronograma(cronograma)
        messagebox.showinfo("Sucesso", "Nome do cronograma cadastrado com sucesso!")
        janela_cronograma.destroy()
    
    janela_cronograma = tk.Toplevel(root)
    janela_cronograma.title("Cadastrar Nome do Cronograma")
    janela_cronograma.geometry("300x200")

    tk.Label(janela_cronograma, text="Nome do Cronograma:").pack(pady=10)
    entry_cronograma = tk.Entry(janela_cronograma)
    entry_cronograma.pack(pady=10)

    tk.Button(janela_cronograma, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_cronograma_aula():
    def submit():
        nome_cronograma = entry_nome_cronograma.get()
        id_horario_aula = entry_id_horario_aula.get()
        id_nome_cronograma = entry_id_nome_cronograma.get()
        id_associacao_materia_curso = entry_id_associacao_materia_curso.get()
        cadastro.cadastrar_cronograma_aula(nome_cronograma, id_horario_aula, id_nome_cronograma, id_associacao_materia_curso)
        messagebox.showinfo("Sucesso", "Cronograma de aula cadastrado com sucesso!")
        janela_cronograma_aula.destroy()
    
    janela_cronograma_aula = tk.Toplevel(root)
    janela_cronograma_aula.title("Cadastrar Cronograma de Aula")
    janela_cronograma_aula.geometry("400x300")

    tk.Label(janela_cronograma_aula, text="Nome do Cronograma:").pack(pady=5)
    entry_nome_cronograma = tk.Entry(janela_cronograma_aula)
    entry_nome_cronograma.pack(pady=5)

    tk.Label(janela_cronograma_aula, text="ID do Horário de Aula:").pack(pady=5)
    entry_id_horario_aula = tk.Entry(janela_cronograma_aula)
    entry_id_horario_aula.pack(pady=5)

    tk.Label(janela_cronograma_aula, text="ID do Nome do Cronograma:").pack(pady=5)
    entry_id_nome_cronograma = tk.Entry(janela_cronograma_aula)
    entry_id_nome_cronograma.pack(pady=5)

    tk.Label(janela_cronograma_aula, text="ID da Associação Matéria-Curso:").pack(pady=5)
    entry_id_associacao_materia_curso = tk.Entry(janela_cronograma_aula)
    entry_id_associacao_materia_curso.pack(pady=5)

    tk.Button(janela_cronograma_aula, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_periodo():
    def submit():
        periodo = entry_periodo.get()
        cadastro.cadastrar_periodo(periodo)
        messagebox.showinfo("Sucesso", "Período cadastrado com sucesso!")
        janela_periodo.destroy()
    
    janela_periodo = tk.Toplevel(root)
    janela_periodo.title("Cadastrar Período")
    janela_periodo.geometry("300x200")

    tk.Label(janela_periodo, text="Digite o período:").pack(pady=10)
    entry_periodo = tk.Entry(janela_periodo)
    entry_periodo.pack(pady=10)

    tk.Button(janela_periodo, text="Cadastrar", command=submit).pack(pady=10)

def chamar_cadastrar_horario_aula():
    def submit():
        nome_horario = entry_nome_horario.get()
        hora_inicio = entry_hora_inicio.get()
        hora_fim = entry_hora_fim.get()
        id_periodo = int(entry_id_periodo.get())
        cadastro.cadastrar_horario_aula(nome_horario, hora_inicio, hora_fim, id_periodo)
        messagebox.showinfo("Sucesso", "Horário de aula cadastrado com sucesso!")
        janela_horario_aula.destroy()
    
    janela_horario_aula = tk.Toplevel(root)
    janela_horario_aula.title("Cadastrar Horário de Aula")
    janela_horario_aula.geometry("400x300")

    tk.Label(janela_horario_aula, text="Nome do Horário:").pack(pady=5)
    entry_nome_horario = tk.Entry(janela_horario_aula)
    entry_nome_horario.pack(pady=5)

    tk.Label(janela_horario_aula, text="Hora de Início (HH:MM:SS):").pack(pady=5)
    entry_hora_inicio = tk.Entry(janela_horario_aula)
    entry_hora_inicio.pack(pady=5)

    tk.Label(janela_horario_aula, text="Hora de Fim (HH:MM:SS):").pack(pady=5)
    entry_hora_fim = tk.Entry(janela_horario_aula)
    entry_hora_fim.pack(pady=5)

    tk.Label(janela_horario_aula, text="ID do Período:").pack(pady=5)
    entry_id_periodo = tk.Entry(janela_horario_aula)
    entry_id_periodo.pack(pady=5)

    tk.Button(janela_horario_aula, text="Cadastrar", command=submit).pack(pady=10)

def exibir_menu_admin():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin - Menu de Cadastro")
    admin_window.geometry("900x900")

    tk.Button(admin_window, text="Cadastrar Titularidade", command=chamar_funcao(chamar_cadastrar_titularidade)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Professor", command=chamar_funcao(chamar_cadastrar_professor)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Área do Curso", command=chamar_funcao(chamar_cadastrar_area_curso)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Matéria", command=chamar_funcao(chamar_cadastrar_materia)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Curso", command=chamar_funcao(chamar_cadastrar_curso)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Semestre", command=chamar_funcao(chamar_cadastrar_semestre)).pack(fill='x')
    tk.Button(admin_window, text="Associar Professor com Matéria", command=chamar_funcao(chamar_associar_professor_materia)).pack(fill='x')
    tk.Button(admin_window, text="Associar Matéria com Curso", command=chamar_funcao(chamar_associar_materia_curso)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Nome Cronograma", command=chamar_funcao(chamar_cadastrar_nome_cronograma)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Período", command=chamar_funcao(chamar_cadastrar_periodo)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Horário de Aula", command=chamar_funcao(chamar_cadastrar_horario_aula)).pack(fill='x')
    tk.Button(admin_window, text="Cadastrar Cronograma de Aula", command=chamar_funcao(chamar_cadastrar_cronograma_aula)).pack(fill='x')
    tk.Button(admin_window, text="Sair", command=admin_window.destroy).pack(fill='x')

def conectar_banco():
    try:
        conexao_banco = banco_de_dados.conectar_banco_de_dados(banco_de_dados.informacao_conexao_db)
        if not conexao_banco:
            messagebox.showerror("Erro", "Erro ao conectar ao banco de dados.")
            return None

        resultados = banco_de_dados.verificar_existencia_tabelas(conexao_banco, banco_de_dados.TABELAS)
        todas_existem = all(existe for _, existe in resultados)

        if todas_existem:
            print("Todas as tabelas existem.")
        else:
            print("Algumas tabelas não existem. Criando tabelas...")
            banco_de_dados.criar_tabelas_iniciais(conexao_banco)

        return conexao_banco
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados ou ao verificar/criar tabelas: {e}")
        return None

def main():
    conexao_banco = conectar_banco()
    if conexao_banco is None:
        return

    def chamar_gerar_horario():
        gerar_horario.main()
        messagebox.showinfo("Info", "Horário Escolar Gerado")

    tk.Button(root, text="Gerar Horário Escolar", command=chamar_gerar_horario).pack(fill='x')
    tk.Button(root, text="Administrador", command=exibir_menu_admin).pack(fill='x')
    tk.Button(root, text="Sair", command=root.destroy).pack(fill='x')

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("900x900")
    main()