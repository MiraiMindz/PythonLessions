<!-- #region OldCode -->

Tipos de Controle de Flow e Escopo

Sequencial: o código é executado de forma sequencial, cima a baixo

Decisivo: o código é executado baseado em uma decisão, if statements

Repetitivo: o código é executado em loop, while e for loops

Funcional: o código é dividido e executado em forma de funções (veremos mais a frente)


(x) Sequencial
(x) Decisivo
( ) Repetitivo
( ) Funcional

Verdadeiros:
- True
- qualquer string que não esteja vazia
- qualquer numero diferente de 0
- qualquer outro tipo de dado que não esteja vazio

Falsos:
- False
- Strings vazias ("" ou '')
- 0
- qualquer outro tipo de dado vazio

cadeias de `elif` e `match-case`

> NOTA: o match-case foi introduzido python 3.10

if (condição):
    {codigo}

if == se

se

`else` -> se não

ESCOPO:

"Niveis" do programa

1. Global
2. Escopos Internos


1. Global
2. A
3. B
4. C

GLOBAL
A {
    ESCOPO DE {NOME DA FUNÇÃO/FLOW}
    x = 3
    print(y)
    B {
        ESCOPO DE B
        print(x)
        C {
            ESCOPO DE C
            print(x)
            y = 1
        }
    }
}



CAIXA_EXTERNA={

    print(x)

    CAIXA_MEDIANA={

        print(x)

        CAIXA_INTERNA={

            x = 3

        }
    }
}


se o nome é igual a 'mirai'
se o nome é igual a 'kaal'
se o nome não igual a nenhum.

elif -> else-if

entra

match {variavel}:
    case {possiveis valores}:
        {codigo}
    case _:
        {codigo}



lista=[
    dict_01={
        x=23
    }
    dict_02={
        x=32
    }
]
lista=[
    dict_01={
        x=24
    }
    dict_02={
        x=32
    }
]
lista=[
    dict_01={
        x=23
    }
    dict_02={
        x=44
    }
]


Controle de Fluxo (Control Flow) e Escopo
(x) Sequencial
(x) Decisivo
( ) Repetitivo
( ) Funcional

se e se não

se {nome} estiver em {lista_amigos} exibir "Ola amigo", caso contrário, exibir "Ola estranho"

`if` e o `else`

if {condição}:
    {codigo} # SE FOR SIM
else:
    {codigo} # SE FOR NÃO


== -> é igual?

x == y -> x é igual a y?

!= -> não igual/diferente

ESCOPO

O Escopo é sempre de fora para dentro, nunca de dentro para fora.

1. Global
2. A
3. B
4. C

GLOBAL {
x = 3
    A {
        print(x)
        B {
            print(x)
            C {
                print(x)
            }
        }
    }
}

GLOBAL
x = 3
    A
        print(x)
        B
            print(x)
            C
                print(x)

match {variavel}:
    case {possivel valor}:
        {codigo}
    case {possivel valor}:
        {codigo}
    case {possivel valor}:
        {codigo}
    case _:
        {codigo}


<!-- #endregion -->
