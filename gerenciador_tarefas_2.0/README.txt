
# Gerenciador de Tarefas Simples

Este é um projeto de um Gerenciador de Tarefas Simples desenvolvido em Python. A aplicação permite ao usuário adicionar, listar, marcar como completas e remover tarefas através de um menu interativo no terminal. Agora, com a segunda versão, as tarefas são persistidas em um banco de dados SQLite, garantindo que os dados sejam mantidos entre as execuções do programa.

## Funcionalidades

- **Adicionar Tarefas:** Permite adicionar uma nova tarefa especificando o nome e a descrição.
- **Listar Tarefas:** Exibe todas as tarefas adicionadas, indicando se estão completas ou não.
- **Marcar como Completa:** Permite marcar uma tarefa específica como concluída.
- **Remover Tarefas:** Permite remover uma tarefa da lista.

### Novas Funcionalidades na Versão 2.0

- **Persistência de Dados:** Agora, as tarefas são armazenadas em um banco de dados SQLite, permitindo que as informações sejam salvas e acessadas posteriormente, mesmo após o fechamento da aplicação.
- **CRUD com SQLAlchemy:** O projeto utiliza SQLAlchemy para gerenciar as operações de criação, leitura, atualização e exclusão (CRUD) de tarefas no banco de dados.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que gerencia as interações do usuário com o sistema.
- **`tarefa.py`**: Módulo que define a classe `Tarefa`, com atributos para nome, descrição e status de completude.
- **`crud.py`**: Módulo que contém as funções para manipulação das tarefas no banco de dados (adicionar, listar, completar e remover).
- **`database.py`**: Módulo que configura o banco de dados SQLite usando SQLAlchemy, definindo o modelo `Tarefa` e gerenciando a sessão de conexão.

## Como Usar

1. Clone o repositório ou faça o download dos arquivos.
2. Certifique-se de ter o Python instalado na sua máquina.
3. Execute o arquivo `main.py` para iniciar o gerenciador de tarefas:

   ```bash
   python main.py
   ```

Agora, ao adicionar, listar, marcar como completa ou remover tarefas, todas as mudanças serão refletidas diretamente no banco de dados, mantendo a integridade dos dados mesmo após o encerramento do programa.
