# crud.py
from .database import session, Tarefa  # Uso do import relativo para corrigir o erro de importação
import tkinter as tk
from tkinter import messagebox


# Função para adicionar uma tarefa
def adicionar_tarefa(descricao):
    nova_tarefa = Tarefa(descricao=descricao, completa=False)  # Corrigir para passar os argumentos corretamente
    session.add(nova_tarefa)
    session.commit()  # Adicionar os parênteses para executar o commit
    print('✅ Tarefa adicionada com sucesso!')

# Função para listar as tarefas existentes
def listar_tarefas():
    tarefas = session.query(Tarefa).all()
    return tarefas

# Função para completar uma tarefa
def completar_tarefa(tarefa_id):
    tarefa = session.query(Tarefa).get(tarefa_id)
    if tarefa:
        tarefa.completa = True
        session.commit()
        print(f'✅ Tarefa "{tarefa.descricao}" marcada como completa!')
    else:
        print('Tarefa não encontrada!')

# Função para remover uma tarefa
def remover_tarefa(tarefa_id):
    tarefa = session.query(Tarefa).get(tarefa_id)
    if tarefa:
        session.delete(tarefa)
        session.commit()
        print(f'✅ Tarefa "{tarefa.descricao}" removida com sucesso!')
    else:
        print('Tarefa não encontrada!')
