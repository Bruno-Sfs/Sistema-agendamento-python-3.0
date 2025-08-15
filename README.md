# Sistema de Agendamento de Clientes

Este é um projeto de desenvolvimento web para um sistema de agendamento de clientes, criado como parte dos meus estudos no curso de Análise e Desenvolvimento de Sistemas. O objetivo é aplicar conhecimentos em Python, Django, Git e, futuramente, JavaScript e AWS, para construir uma aplicação web completa e funcional.

## Status do Projeto

:construction: **Em Desenvolvimento** :construction:

Atualmente, o projeto concluiu a **Fase 1**, que consiste na estruturação do backend e do banco de dados. A aplicação ainda não possui uma interface para o usuário final (frontend).

## Funcionalidades Implementadas (Fase 1)

* **Backend com Django:** Estrutura do projeto criada e configurada.
* **Banco de Dados:** Modelagem das tabelas para `Clientes`, `Serviços` e `Agendamentos`.
* **Painel de Administração:** Uma área administrativa (`/admin`) totalmente funcional que permite:
    * Cadastrar, visualizar, editar e deletar Clientes.
    * Cadastrar, visualizar, editar e deletar Serviços.
    * Criar, visualizar, editar e deletar Agendamentos, associando clientes e serviços.

## Tecnologias Utilizadas (Até o momento)

* **Linguagem:** Python 3
* **Framework Backend:** Django
* **Banco de Dados (desenvolvimento):** SQLite3
* **Controle de Versão:** Git & GitHub

## Como Executar o Projeto Localmente

Para rodar este projeto em sua máquina, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o painel de admin:**
    ```bash
    python manage.py createsuperuser
    ```
    (Siga as instruções para criar seu usuário e senha)

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o painel de administração** no seu navegador em: `http://127.0.0.1:8000/admin/`

## Próximos Passos (Fase 2)

- [ ] Desenvolvimento do **Frontend** com HTML, CSS e JavaScript.
- [ ] Criação de uma interface para o usuário final visualizar, criar e gerenciar agendamentos.
- [ ] Conexão do Frontend com o Backend através de uma API.