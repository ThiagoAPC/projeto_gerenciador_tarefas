from colorama import Fore, Style, init

# Inicializa o colorama para Windows
init(autoreset=True)

# Lista global para armazenar as tarefas
lista_tarefas = []

def adicionar_tarefa():
    nova_tarefa = {}
    nova_tarefa['descricao'] = input(Fore.YELLOW + 'Descrição da Tarefa: ')
    nova_tarefa['completa'] = False  # Inicia como não completa
    lista_tarefas.append(nova_tarefa)  # Adiciona a nova tarefa à lista
    print(Fore.GREEN + '✅ Tarefa adicionada com sucesso!')

def listar_tarefas():
    print(Fore.CYAN + '-' * 40)
    if not lista_tarefas:  # Verifica se a lista está vazia
        print(Fore.RED + 'Nenhuma tarefa encontrada.')
    else:
        for i, tarefa in enumerate(lista_tarefas, start=1):  # Usando enumerate para pegar o índice
            status = '✔' if tarefa['completa'] else '✘'  # Mostra se a tarefa está completa ou não
            print(Fore.CYAN + f'{i}. {tarefa["descricao"]} [{status}]')
    print(Fore.CYAN + '-' * 40)

def completar_tarefas():
    print(Fore.CYAN + '-' * 40)
    if not lista_tarefas:  # Verifica se tem tarefas
        print(Fore.RED + 'Nenhuma Tarefa Encontrada!')
    else:
        # Lista as Tarefas existentes
        for i, tarefa in enumerate(lista_tarefas, start=1):  # Usando enumerate para pegar o índice
            status = '✔' if tarefa['completa'] else '✘'  # Mostra se a tarefa está completa ou não
            print(Fore.CYAN + f'{i}. {tarefa["descricao"]} [{status}]')

        # Solicita ao usuário que escolha uma das tarefas para marcar como completa
        try:
            numero = int(input(Fore.YELLOW + 'Digite o número de uma das tarefas: '))
            if 1 <= numero <= len(lista_tarefas):
                lista_tarefas[numero-1]['completa'] = True  # Marca a tarefa como concluída
                print(Fore.GREEN + f'✅ Tarefa "{lista_tarefas[numero - 1]["descricao"]}" marcada como completa!')
            else:
                print(Fore.RED + 'Número inválido, por favor tente novamente!')
        except ValueError:
            print(Fore.RED + 'Entrada inválida, por favor insira um número válido!')
    print(Fore.CYAN + '-' * 40)

def remover_tarefa():
    while True:
        print(Fore.CYAN + '-' * 40)
        if not lista_tarefas:  # Verifica se tem tarefas
            print(Fore.RED + 'Nenhuma Tarefa Encontrada')
            break  # Sai do loop se não houver tarefas
        else:
            # Lista as Tarefas existentes
            for i, tarefa in enumerate(lista_tarefas, start=1):  # Usando enumerate para pegar o índice
                status = '✔' if tarefa['completa'] else '✘'  # Mostra se a tarefa está completa ou não
                print(Fore.CYAN + f'{i}. {tarefa["descricao"]} [{status}]')
            
            # Solicita ao usuário que escolha uma das tarefas para remover da lista
            try:
                numero = int(input(Fore.YELLOW + 'Digite o número da tarefa que você quer remover: '))
                if 1 <= numero <= len(lista_tarefas):
                    tarefa_removida = lista_tarefas.pop(numero-1)  # Remove a tarefa usando pop
                    print(Fore.GREEN + f'✅ Tarefa "{tarefa_removida["descricao"]}" removida com sucesso!')
                    break  # Sai do loop após a remoção bem-sucedida
                else:
                    print(Fore.RED + 'Número da tarefa inválido, tente novamente')
            except ValueError:
                print(Fore.RED + 'Entrada inválida, por favor insira um número válido!')
        print(Fore.CYAN + '-' * 40)
