# main.py
from utilidadesCeV.crud import adicionar_tarefa, listar_tarefas, completar_tarefa, remover_tarefa
from colorama import Fore, Style, init
import time

# Inicializa o colorama para Windows
init(autoreset=True)

# Funções principais
def menu_principal():
    print('\n' * 2)
    print(Fore.CYAN + '-' * 40)
    print(Fore.CYAN + '🚀 Sistema de Gerenciamento de Tarefas 🚀')
    print(Fore.CYAN + '-' * 40)
    print(Fore.YELLOW + 'Selecione uma das funcionalidades:')
    print(Fore.GREEN + '1️⃣ - Adicionar Tarefas')
    print(Fore.GREEN + '2️⃣ - Listar Tarefas')
    print(Fore.GREEN + '3️⃣ - Marcar Tarefa como completa')
    print(Fore.GREEN + '4️⃣ - Remover Tarefa')
    print(Fore.RED + '5️⃣ - Sair')
    print(Fore.CYAN + '-' * 40)

def iniciar():
    while True:
        menu_principal()
        opcao = input(Fore.YELLOW + 'Digite o número da sua opção: ')
        print(Fore.CYAN + '-' * 40)
        
        if opcao == '1':
            descricao = input(Fore.YELLOW + 'Descrição da Tarefa: ')
            adicionar_tarefa(descricao)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            listar_tarefas()
            tarefa_id = int(input(Fore.YELLOW + 'Digite o ID da tarefa para marcar como completa: '))
            completar_tarefa(tarefa_id)
        elif opcao == '4':
            listar_tarefas()
            tarefa_id = int(input(Fore.YELLOW + 'Digite o ID da tarefa para remover: '))
            remover_tarefa(tarefa_id)
        elif opcao == '5':
            print(Fore.RED + 'Você escolheu a opção Sair 🚪')
            print(Fore.GREEN + 'Encerrando o programa... Até Logo! 👋')
            for i in range(3, 0, -1):
                print(Fore.GREEN + f'Encerrando em {i}...')
                time.sleep(1)
            break
        else:
            print(Fore.RED + '⚠️ Opção inválida. Tente novamente!')

# Inicia o programa chamando a função iniciar
if __name__ == "__main__":
    iniciar()
