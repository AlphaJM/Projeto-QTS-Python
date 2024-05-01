# Aqui vai ser o arquivo principal do projeto

import dbfunctions
import dbconexao
import tkinter as tk
from tkinter import ttk

# Cria uma janela Tkinter
"""root = tk.Tk()

# Cria um rótulo (label)
label = tk.Label(root, text='Digite o nome para cadastro do professor: ').pack()
entrada = tk.Entry(root)
entrada.pack
# Empacota o rótulo na janela
label.pack()

root.mainloop()"""

def verificar_condicao():
    texto_entrada = entrada.get()
    if texto_entrada.lower() == "olá":
        resultado.config(text="Condição verdadeira!", foreground="green")
    else:
        resultado.config(text="Condição falsa!", foreground="red")

root = tk.Tk()
root.title("Verificador de Condição")

# Adiciona estilo aos widgets
style = ttk.Style()
style.configure("TButton", foreground="black", background="lightgray")
style.configure("TLabel", foreground="black", background="white")

# Criação dos widgets
label = ttk.Label(root, text="Digite 'Olá' na caixa abaixo:")
label.grid(row=0, column=0, padx=10, pady=10)

entrada = ttk.Entry(root)
entrada.grid(row=1, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Verificar", command=verificar_condicao)
botao.grid(row=2, column=0, padx=10, pady=10)

resultado = ttk.Label(root, text="", font=("Arial", 12, "bold"))
resultado.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()

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





'''escolha = int(input("Bem vindo ao sistema de horário, digite o número para a escolha do que fazer: \n1- Cadastrar Professor\n2- Cadastrar Materia\n3- Cadastrar Curso"))

if escolha == 1:
    nome = input("Digite o nome do Professor: ")
    formacao = input("Digite a formação do professor: ")
    dbfunctions.cadastrar_professor(nome, formacao)
'''