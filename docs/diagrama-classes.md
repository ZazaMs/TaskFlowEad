# Diagrama de Classes

## Objetivo

O diagrama representa a estrutura principal do TaskFlow, demonstrando as classes responsáveis pelas tarefas, pelo banco de dados e pelo funcionamento da aplicação.

## Diagrama

```mermaid
classDiagram
    class Tarefa {
        +int id
        +string titulo
        +string descricao
        +string status
        +string prioridade
    }

    class BancoDeDados {
        +conectar()
        +criar_tabela()
        +listar_tarefas()
        +adicionar_tarefa()
        +atualizar_tarefa()
        +excluir_tarefa()
    }

    class Aplicacao {
        +index()
        +criar()
        +editar()
        +excluir()
    }

    Aplicacao --> BancoDeDados : utiliza
    BancoDeDados --> Tarefa : armazena
```

## Descrição das classes

**Tarefa:** representa uma atividade cadastrada no sistema, contendo identificador, título, descrição, status e prioridade.

**BancoDeDados:** responsável por estabelecer a conexão com o SQLite e executar operações de consulta, cadastro, atualização e exclusão de tarefas.

**Aplicacao:** responsável por receber as requisições do usuário por meio das rotas Flask e acionar as operações necessárias no banco de dados.

## Relacionamentos

- Aplicacao utiliza BancoDeDados para realizar as operações.
- BancoDeDados armazena e recupera os registros representados pela entidade Tarefa.
