
# Gerenciador de Tarefas - Versão 3.0

Este é um projeto de um Gerenciador de Tarefas Simples desenvolvido em Python, agora com uma interface gráfica aprimorada para uma experiência de usuário mais moderna e interativa. A aplicação permite ao usuário adicionar, listar, marcar como completas e remover tarefas através de uma interface gráfica amigável.

## Novidades na Versão 3.0
- **Interface Gráfica Modernizada:** Agora com uma interface gráfica usando Tkinter, com botões estilizados, ícones e layout mais intuitivo.
- **Persistência de Dados:** Tarefas são armazenadas em um banco de dados SQLite, garantindo que os dados não sejam perdidos ao fechar o programa.
- **Melhorias de Navegação:** Os elementos da interface estão melhor espaçados e alinhados, proporcionando um uso mais confortável.

## Funcionalidades

- **Adicionar Tarefas:** Permite adicionar uma nova tarefa especificando a descrição. Agora com botão e ícone dedicados.
- **Listar Tarefas:** Exibe todas as tarefas adicionadas, indicando se estão completas ou não, diretamente na interface gráfica.
- **Marcar como Completa:** Permite marcar uma tarefa específica como concluída com um simples clique de botão.
- **Remover Tarefas:** Permite remover uma tarefa da lista de forma intuitiva.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que inicializa a interface gráfica e gerencia as interações do usuário com o sistema.
- **`crud.py`**: Contém as funções para criar, ler, atualizar e deletar tarefas no banco de dados.
- **`database.py`**: Configura o banco de dados SQLite usado pela aplicação para armazenar as tarefas.
- **`icons/`**: Pasta contendo os ícones utilizados na interface gráfica para melhorar a experiência do usuário.

## Como Usar

1. Clone o repositório ou faça o download dos arquivos.
2. Certifique-se de ter o Python instalado na sua máquina e todos os pacotes necessários (como `tkinter` e `PIL`).
3. Execute o arquivo `main.py` para iniciar o gerenciador de tarefas:

   ```bash
   python main.py
   ```

4. Utilize a interface gráfica para gerenciar suas tarefas de forma fácil e rápida!

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `Pillow`
