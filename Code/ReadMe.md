# Codigo das Aulas

Nessa pasta se existiram os codigos e os arquivos das aulas.

Ela segue o seguinte esquema:

```
${SEU NOME}/
└─ ${SEÇÃO/CAPITULO}/
    └─ ${SEÇÃO/CAPITULO}_${SEU NOME}.py ou ${SEÇÃO/CAPITULO}_${SEU NOME}.md
```

exemplo:

```
Mirai/
├─ FundamentosI/
│  ├─ FundamentosI_Mirai.py
│  └─ FundamentosI_Mirai.md
└─ OrientacaoObjetosBase/
   ├─ OrientacaoObjetosBase_Mirai.py
   └─ OrientacaoObjetosBase_Mirai.md
```

> Dica: Evitem usar Espaços no nome do arquivo, facilta caso tenhamos que usa-lo em um terminal

Você também pode usar o script `GenFile.py` para gerar essa estrutura.

```
Uso:
    python3 generate_files.py [-h] [-n] [-c] name cap_num

Um script feito para automatizar/padronizar a criação de arquivos pertinentes as aulas.

Options:
    -h, --help              Exibe esta ajuda
    -n, --name              Especifica o nome
    -c, --cap_num           Especifica o numero do capitulo

As opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero do capitulo seguindo a ordem
Caso nenhum argumento seja provido você será perguntado dentro do script

Exemplos de Uso:
    1.      python3 generate_files.py -n Mirai -c 1
    2.      python3 generate_files.py Mirai 1
    3.      python3 generate_files.py
```
