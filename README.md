# LocBike2.0

LocBike2.0 foi criado como um projeto final do terceiro semestre do curso técnico de informática. Este projeto visa fornecer uma solução prática para a locação de bicicletas, facilitando o processo tanto para locadores quanto para locatários.

## Estórias do Usuário

1. **Como um locador, quero poder cadastrar minhas bicicletas para locação, para que outras pessoas possam alugá-las.**
2. **Como um locatário, quero poder pesquisar e alugar bicicletas disponíveis, para que eu possa utilizá-las quando necessário.**
3. **Como um administrador, quero gerenciar os usuários e as bicicletas cadastradas, para manter o sistema organizado e seguro.**

## Pacote

Este projeto está estruturado da seguinte forma:

- `__pycache__/` - Diretório de cache do Python.
- `instance/uploads/` - Diretório para uploads de arquivos.
- `Diagrama.pdf` - Arquivo PDF com o diagrama do projeto.
- `README.md` - Este arquivo README.
- `config.py` - Arquivo de configuração do projeto.
- `flask_app.py` - Arquivo principal da aplicação Flask.

## Protótipo

O protótipo da aplicação foi desenvolvido utilizando ferramentas de design para visualizar a interface do usuário e o fluxo da aplicação. Ele pode ser encontrado na seção de documentos do projeto.

## Requisitos de Usuário

1. **Cadastro de Usuário:** O sistema deve permitir que novos usuários se cadastrem.
2. **Autenticação:** O sistema deve permitir que usuários existentes façam login.
3. **Cadastro de Bicicletas:** Usuários autenticados devem poder cadastrar suas bicicletas para locação.
4. **Pesquisa de Bicicletas:** Usuários devem poder pesquisar bicicletas disponíveis para locação.
5. **Aluguel de Bicicletas:** Usuários devem poder alugar bicicletas disponíveis.
6. **Administração:** Administradores devem ter a capacidade de gerenciar usuários e bicicletas cadastradas.

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/locbike2.0.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd locbike2.0
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados e as variáveis de ambiente no arquivo `config.py`.

6. Execute a aplicação:
    ```bash
    python flask_app.py
    ```

A aplicação estará disponível em `http://localhost:5000`.

## Contribuição

Se você deseja contribuir para este projeto, por favor, siga as diretrizes de contribuição.
