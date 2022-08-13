# Milestones

Essa pasta serve para colocarmos as Milestones (Projetos).

Ela segue o seguinte esquema:

```
${SEU NOME}/
└─ ${NOME DO PROJETO/MILESTONE}/
   └─ main.py
```

exemplo:

```
Mirai/
└─ BibliotecaLivros/
   └─ main.py
```

> Dica: Evitem usar Espaços no nome do arquivo, facilta caso tenhamos que usa-lo em um terminal

Você também pode usar o script `GenMilestones.py` para gerar essa estrutura.

```
Uso:
        python3 GenMilestones.py [-h] [-n] [-c] name cap_num

Um script feito para automatizar/padronizar a criação de arquivos pertinentes as milestones.

Options:
        -h, --help              Exibe esta ajuda
        -n, --name              Especifica o nome
        -n, --cap_num           Especifica o numero da milestone

As opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero da milestone seguindo a ordem
Caso nenhum argumento seja provido você será perguntado dentro do script

Exemplos de Uso:
        1.      python3 GenMilestones.py -n Mirai -c 1
        2.      python3 GenMilestones.py Mirai 1
        3.      python3 GenMilestones.py
```

## Lista de Milestones

- Milestone 1
  - Criar a Biblioteca de Filmes
- Milestone 2
  - Criando Biblioteca de Livros
- Milestone 3
  - Introdução ao Scraper de Citações
- Milestone 4
  - Um Scraper de Livros + Desenvolvimento de Aplicação
- Milestone 5
  - Um bot pro discord usando o `discord.py`
- Milestone 6
  - Criando um Editor de Texto
- Milestone 7
  - Um App de Pintura
- Milestone 8
  - Escrevendo um Perceptron
- Milestone 9
  - TCP Chat Room
- Milestone 10
  - TCP Chat Room Criptografada
- Milestone 11
  - Cliente Torrent
