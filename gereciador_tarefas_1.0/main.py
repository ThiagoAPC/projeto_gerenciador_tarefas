# Arquivo principal de execução do programa
from utilidadesCeV.tarefa import adicionar_tarefa, listar_tarefas, completar_tarefas, remover_tarefa
from colorama import Fore, Style, init
import time

# Inicializa o colorama para Windows
init(autoreset=True)

# Funções principais
def menu_principal():
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
    while True:  # Definindo o loop de escolha de opções
        menu_principal()  # Iniciando o menu principal
        opcao = input(Fore.YELLOW + 'Digite o número da sua opção: ')
        print(Fore.CYAN + '-' * 40)
        
        if opcao == '1':
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.BLUE + 'Você escolheu a opção Adicionar Tarefas 📋')
            adicionar_tarefa()
        elif opcao == '2':
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.BLUE + 'Você escolheu a opção Listar Tarefas 📋')
            listar_tarefas()
        elif opcao == '3':
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.BLUE + 'Você escolheu a opção Marcar Tarefa como completa ✅')
            completar_tarefas()
        elif opcao == '4':
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.BLUE + 'Você escolheu a opção Remover Tarefa ❌')
            remover_tarefa()
        elif opcao == '5':
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.RED + 'Você escolheu a opção Sair 🚪')
            print(Fore.GREEN + 'Encerrando o programa... Até Logo! 👋')
            for i in range(3, 0, -1):
                print(Fore.GREEN + f'Encerrando em {i}...')
                time.sleep(1)  # Espera 1 segundo entre cada contagem
            break  # Sai do loop para encerrar o programa
        else:
            print('\n' * 1)  # Adiciona uma linha de espaço
            print(Fore.RED + '⚠️ Opção inválida. Tente novamente!')

# Inicia o programa chamando a função iniciar
if __name__ == "__main__":
    iniciar()
