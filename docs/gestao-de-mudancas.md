# Registro de mudança de escopo

## Escopo original

A primeira versão do TaskFlow previa cadastrar, consultar, editar e excluir tarefas.

## Mudança solicitada

Durante a organização das atividades, percebeu-se que apenas listar as tarefas não ajudaria a equipe a identificar rapidamente o que precisava de atenção. O escopo foi ampliado para incluir:

- Prioridade baixa, média ou alta.
- Filtro da listagem por status.

## Justificativa

Esses recursos ajudam a equipe a visualizar primeiro as atividades mais importantes e acompanhar o andamento sem precisar procurar manualmente na lista.

## Impacto no projeto

Foram adicionados campos e validações no cadastro e na edição, opções de filtro na tela inicial e testes para conferir o funcionamento. No GitHub Projects, deve ser criado um card para essa melhoria e movido para Concluído após a implementação e validação.

## Simulação de mudança de escopo

Durante o desenvolvimento do TaskFlow, foi identificada a necessidade de melhorar a organização das tarefas da equipe.

Inicialmente, o sistema permitia cadastrar, editar e excluir tarefas. Porém, surgiu a necessidade de identificar quais atividades deveriam receber mais atenção.

Mudança solicitada: inclusão de um sistema de prioridades para as tarefas.

Nova funcionalidade: classificação das tarefas em três níveis:

Baixa;

Média;

Alta.

Justificativa: facilitar a organização das atividades e ajudar os usuários a identificar tarefas mais urgentes.

Impacto no projeto: atualização dos requisitos, inclusão de um novo card no Kanban e registro da mudança na documentação.

Resultado esperado: permitir uma visualização mais organizada das tarefas conforme seu nível de prioridade.

A mudança foi registrada no Kanban como um novo item, representando a solicitação adicional de escopo.