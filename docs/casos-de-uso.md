# Diagrama de Casos de Uso

O diagrama representa as ações disponíveis para uma pessoa que utiliza o TaskFlow. Na versão atual, não existe diferenciação entre perfis de usuário.

```mermaid
flowchart LR
    U[Usuário]
    subgraph Sistema TaskFlow
      A((Cadastrar tarefa))
      B((Visualizar tarefas))
      C((Editar tarefa))
      D((Excluir tarefa))
      E((Filtrar por status))
    end
    U --- A
    U --- B
    U --- C
    U --- D
    U --- E
```

**Descrição:** o usuário pode cadastrar, consultar, editar e excluir tarefas. Também pode filtrar a listagem pelo status.
