# Diagrama de Classes

O modelo abaixo representa a entidade principal persistida no banco de dados e os componentes responsáveis pelo acesso aos dados e pelas rotas da aplicação.

```mermaid
classDiagram
    class Tarefa {
      +int id
      +str titulo
      +str descricao
      +str status
      +str prioridade
      +datetime criado_em
    }
    class BancoDeDados {
      +conectar()
      +inicializar()
      +consultar_tarefas()
      +salvar_tarefa()
      +atualizar_tarefa()
      +excluir_tarefa()
    }
    class Aplicacao {
      +listar_tarefas()
      +cadastrar_tarefa()
      +editar_tarefa()
      +remover_tarefa()
    }
    Aplicacao --> BancoDeDados
    BancoDeDados --> Tarefa
```

**Descrição:** `Tarefa` representa os dados armazenados. `BancoDeDados` concentra a conexão e as operações SQLite. `Aplicacao` recebe as solicitações feitas pelas páginas e aciona as operações necessárias.
