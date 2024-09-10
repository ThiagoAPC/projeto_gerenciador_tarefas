import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utilidadesCeV.crud import adicionar_tarefa, listar_tarefas, completar_tarefa, remover_tarefa

def adicionar():
    descricao = entry.get()
    if descricao:
        adicionar_tarefa(descricao)
        entry.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Tarefa adicionada!")
        listar()
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma descrição.")

def listar():
    tarefas = listar_tarefas()
    lista.delete(0, tk.END)
    for tarefa in tarefas:
        status = '✔' if tarefa.completa else '✘'
        lista.insert(tk.END, f"{tarefa.id}. {tarefa.descricao} [{status}]")

def completar():
    try:
        selected = lista.curselection()[0]
        tarefa_id = int(lista.get(selected).split(".")[0])
        completar_tarefa(tarefa_id)
        listar()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para completar.")

def remover():
    try:
        selected = lista.curselection()[0]
        tarefa_id = int(lista.get(selected).split(".")[0])
        remover_tarefa(tarefa_id)
        listar()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("370x470")  # Ajuste do tamanho da janela para se adaptar ao espaçamento
root.configure(bg="#ADD8E6")  # Background azul claro

# Função para carregar ícones
def carregar_icone(caminho, tamanho=(24, 24)):
    imagem = Image.open(caminho)
    imagem = imagem.resize(tamanho, Image.ANTIALIAS)
    return ImageTk.PhotoImage(imagem)

# Carregando ícones
icone_adicionar = carregar_icone("icons/Adicionar_icon.png")
icone_listar = carregar_icone("icons/Listar_icon.png")
icone_completar = carregar_icone("icons/Completar_icon.png")
icone_remover = carregar_icone("icons/Remover_icon.png")

# Entrada de descrição da tarefa
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=(10, 5), padx=5, anchor="w")  # Adiciona espaçamento vertical e horizontal

# Estilos para botões
button_style = {
    "bg": "white", 
    "fg": "black", 
    "font": ("Arial", 10, "bold"), 
    "borderwidth": 1, 
    "relief": "solid", 
    "compound": "left", 
    "anchor": "w",  # Alinha o conteúdo do botão à esquerda
    "padx": 5,
}

# Criando botões com bordas arredondadas e espaçamento
btn_adicionar = tk.Button(root, text=" Adicionar Tarefa", command=adicionar, image=icone_adicionar, **button_style)
btn_adicionar.pack(pady=5, padx=5, anchor="w")  # Alinha o botão à esquerda com espaçamento

btn_listar = tk.Button(root, text=" Listar Tarefas", command=listar, image=icone_listar, **button_style)
btn_listar.pack(pady=5, padx=5, anchor="w")  # Alinha o botão à esquerda com espaçamento

btn_completar = tk.Button(root, text=" Marcar como Completa", command=completar, image=icone_completar, **button_style)
btn_completar.pack(pady=5, padx=5, anchor="w")  # Alinha o botão à esquerda com espaçamento

btn_remover = tk.Button(root, text=" Remover Tarefa", command=remover, image=icone_remover, **button_style)
btn_remover.pack(pady=5, padx=5, anchor="w")  # Alinha o botão à esquerda com espaçamento

# Lista de tarefas
lista = tk.Listbox(root, width=40, height=10, font=("Arial", 10))
lista.pack(pady=(10, 20), padx=5, anchor="w")  # Alinha a lista à esquerda com espaçamento

# Executando a aplicação
root.mainloop()
