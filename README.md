# TaskFlow

Sistema web simples para organizar tarefas de uma equipe. O projeto foi desenvolvido como atividade acadêmica de Engenharia de Software, simulando a organização de demandas de uma equipe de logística.

## Objetivo

Permitir que os usuários cadastrem tarefas, definam prioridades e acompanhem o andamento de cada atividade em um só lugar.

## Escopo inicial

- Cadastrar tarefas com título, descrição e prioridade.
- Consultar a lista de tarefas.
- Editar informações e status.
- Excluir tarefas.
- Filtrar tarefas pelo status.

## Tecnologias

- Python 3.12+
- Flask
- SQLite
- HTML e CSS
- Pytest
- GitHub Actions

## Como executar localmente

1. Instale o Python 3.12 ou superior.
2. Clone este repositório e abra a pasta no terminal.
3. Crie um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

4. Ative o ambiente virtual:

   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**
   ```bash
   source .venv/bin/activate
   ```

5. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

6. Inicie a aplicação:

   ```bash
   python app.py
   ```

7. Acesse `http://127.0.0.1:5000` no navegador.

O banco SQLite é criado automaticamente na primeira execução.

## Executar os testes

Com o ambiente virtual ativado, execute:

```bash
pytest -v
```

Os testes verificam a abertura da página inicial, cadastro, validação de título, atualização e exclusão de tarefas. O GitHub Actions executa essa mesma suíte a cada push e pull request.

## Organização das pastas

```text
taskflow/
├── .github/workflows/tests.yml
├── docs/
│   ├── casos-de-uso.md
│   ├── diagrama-classes.md
│   └── gestao-de-mudancas.md
├── static/style.css
├── templates/
│   ├── base.html
│   └── index.html
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── app.py
├── database.py
├── requirements.txt
└── README.md
```

## Metodologia de trabalho

Foi utilizado o método Kanban por meio do GitHub Projects para organizar e acompanhar as atividades do projeto.

O quadro foi dividido em três colunas: **A Fazer**, **Em Progresso** e **Concluído**. As atividades foram registradas em cards e movimentadas conforme o andamento do desenvolvimento.

## Mudança de escopo

Durante o planejamento e desenvolvimento, foi identificada a necessidade de melhorar a organização das tarefas por meio de níveis de prioridade.

Com isso, o sistema passou a permitir a classificação das atividades em baixa, média e alta prioridade. Essa alteração foi registrada na documentação e representada por um novo card no GitHub Projects.

A mudança demonstra como um requisito adicional pode ser incorporado ao planejamento de um projeto.

## Qualidade e integração contínua

Os testes automatizados foram escritos com Pytest. O workflow em `.github/workflows/tests.yml` instala as dependências e executa os testes em um ambiente Ubuntu sempre que há push ou pull request.

## Limitações atuais

O sistema é uma versão acadêmica inicial. Ainda não possui cadastro de usuários, autenticação, permissões ou publicação em servidor. O banco de dados é local.

## Próximas melhorias

- Adicionar autenticação de usuários.
- Permitir atribuir tarefas a integrantes da equipe.
- Criar um painel com resumo das tarefas por status.
