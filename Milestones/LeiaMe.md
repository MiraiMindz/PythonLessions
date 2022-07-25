# Milestone 01

Quantos filmes você já assistiu?

Bom, não precisa me responder mas imagino que você tenha assistido ao menos um filme...

E se existisse uma forma de você "guardar" esse filme? Pois então este será seu desafio, você irá programar uma biblioteca de filmes.

O seu objetivo é deixar igual ao video que eu enviei.

---

Antes de começar eu gostaria que você fizesse algumas coisas:
- Crie um arquivo chamado `app.py`
- Escreva uma "DocString de Projeto/Teste"
- Documente quaisquer função que você criar usando DocStrings

O que seria essa "DocString de Projeto/Teste"?

é essencialmente um "cabeçalho" contendo informações como:
- Titulo (O Nome do Projeto)
- Objetivo (O motivo da criação do projeto)
- Descrição curta do projeto (entre 1 e 7 linhas)
- Lista de Tarefas (TODOs) (uma serie de etapas para concluir o projeto)
- Autor
- Data (Data de Inicio - Data de Finalização)

Aqui é um exemplo de um "cabeçalho" de outro projeto:

```py
''' Playground de Arvore Binária
    Esse programa foi escrito como desafio final no curso de Python.
    Um programa que gera, organiza, adiciona, exclui e exibe Arvores Binárias.

TODO:
    [x] - Criar os Nodes
    [x] - Implementar algoritmo base
    [x] - Menu
    [x] - Implementar algoritmos extras
    [x] - Implementar Formatação
    [ ] - Refatorar

AUTOR: Mirai
DATA: 12/10/21 - 14/10/21'''
```

---

## Dicas e Requerimentos

Como essa é sua primeira milestone eu irei colocar dicas e algumas coisas que eu quero que você faça

### Requerimentos

- Um menu usando `while` loop
- As opções devem ser divididas em funções

### Dicas

para limpar o console via python basta printar `\033c`, ou adicionar esta linha de codigo:
```py
print("\033c", end='')
```
