# Gerenciador de Tarefas - Versão 3.0

Esta versão do Gerenciador de Tarefas traz um layout totalmente novo com uma interface gráfica aprimorada para uma melhor experiência do usuário.

## Novidades na Versão 3.0
- **Interface gráfica modernizada**: agora com um layout mais limpo, botões estilizados e ícones para facilitar a navegação.
- **Persistência de Dados**: todas as tarefas são armazenadas em um banco de dados SQLite, garantindo que nada se perca ao fechar o programa.
- **Melhorias de Navegação**: espaçamento e alinhamento aprimorados para uma interface mais agradável e fácil de usar.

## Estrutura do Projeto
- **main.py**: Arquivo principal que inicializa a interface gráfica do Gerenciador de Tarefas.
- **crud.py**: Contém as funções de criar, ler, atualizar e deletar tarefas do banco de dados.
- **database.py**: Configura o banco de dados SQLite usado pelo programa.
- **icons/**: Pasta contendo os ícones usados na interface gráfica.

## Como Usar
1. Clone o repositório ou faça o download dos arquivos.
2. Certifique-se de ter o Python instalado na sua máquina.
3. Execute o arquivo `main.py` para iniciar o gerenciador de tarefas:

```bash
python main.py
