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


3. Global
4. A
5. B
6. C

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

- [x] Sequencial
- [x] Decisivo
- [ ] Repetitivo
- [ ] Funcional

== é igual?
!= não é igual? / diferente

2 keyword

while -> ENQUANTO algo for verdade executar isso.

x = 0 -> incialize a variavel x com o valor 0
while x < 10: -> enquanto x for menor que 10, execute o código abaixo
    print(f"valor de x: {x}") -> exiba a string "valor de x: {x}"
    x += 1 -> aumente x por 1 unidade

for -> PARA

for {index} in {raio}:
    {codigo}


*PERFORMANCE*
suponhamos o seguinte, você quer exibir os numeros entre 1 e 100000000 usando um loop, mas quer fazer isso de forma eficiente, como você fará?

A desestruturação em Python consiste em assimilar os valores de um iterável a variaveis

`break`, `continue` e `else` em for loops

x = 1

== é igual?

Escrevam um programa que retorna 'Fizz' caso o numero seja divisivel por 3, 'Buzz' caso ele seja divisivel por 5 e 'FizzBuzz' caso ele seja divisivel por 3 e 5 em um raio de 100 numeros.

- [x] Sequencial
- [x] Decisivo
- [ ] Repetitivo
- [ ] Funcional

2 Keywords

Keyword == palavra reservada

while -> Executar um codigo ENQUANTO algo for verdade.

x = 0
while x < 10:
    print(x)
    x = x + 1

1. loop | x = 0
x = 0
while 0 < 10:
    print(x)
    x = 0 + 1

2. loop
x = 1
while 1 < 10:
    print(x)
    x = 1 + 1

3. loop
x = 2
while 2 < 10:
    print(x)
    x = 2 + 1

(...)

10. loop
x = 10
while 10 < 10:
    print(x)
    x = 10 + 1

for -> PARA algo em tanto


suponhamos o seguinte, você quer exibir os numeros entre 1 e 100000000 usando um loop, mas quer fazer isso de forma eficiente, como você fará?

break, continue e else

Fatiar lista: pegar um pedaço delimitado da lista


lista[inicio:final]

inicio -> INCLUDENTE
final -> EXCLUDENTE

porque {index final+1}? pois o valor será onde a lista acabará, e portanto, não se encontrará incluso, então para incluirmos ele, basta adicionar 1 ao index


Compreensões consistem em gerar um novo elemento com base em um tipo de dado composto atráves de ifs, elses e for loops, comumente dizemos ser uma geração dinamica.



lista_base = ['expr_saida' for 'var' in 'iteravel']
lista_condicao = ['expr_saida' for 'var' in 'iteravel' if (condição)]


Listas
    - Base: lista_resultado = ['expr_saida' for 'var' in 'iteravel']
    - Condicional: lista_resultado = ['expr_saida' for 'var' in 'iteravel' if (condição)]
Sets
    - Base: set_resultado = {'expr_saida' for 'var' in 'iteravel'}
    - Condicional: set_resultado = {'expr_saida' for 'var' in 'iteravel' if (condição)}
Dicionários
    - Base: dict_resultado = {'chave':'valor' for '(chave, valor)' in 'iteravel'}
    - Condicional: dict_resultado = {'chave':'valor' for '(chave, valor)' in 'iteravel' if ('chave' satisfaz condição)}

{'chave':'valor' for '(chave, valor)' in 'iteravel' if ('chave' satisfaz condição)}



A função zip() junta elementos de multiplos iteráveis em tuples.

(1 - a)
(2 - b)
(3 - c)
(4 - d)
(5 - e)


A diferença entre a função zip() e a função enumerate() é que a função enumerate() enumera um iterável, enquanto a função zip() junta multiplos iteráveis

def {NOME}():
    {CODIGO}

posicionais
argumento-chave


*args, **kwargs, * (Keyword Only Arguments) e / (Positional Only Arguments)

lambda {ARGUMENTOS} : {EXPRESSÂO}

Função de Primeira Classe -> Tratar como variavel

a {
    b {
        c {
            d {
                return 3
            }
        }
    }
}

nonlocal | global

Variable Shadowing ocorre quando uma variavel de um escopo interno tem o mesmo nome que uma variavel de um escopo externo, isso pode levar a erros e a comportamentos não esperados no código então deve ser evitado. O recomendado é declarar variaveis internas com outros nomes, ou melhor ainda, não usar variaveis globais.


- [x] Funções Lambda
- [x] Funções de Primeira Classe
- [x] Funções de Alta Ordem
- [x] Keyword de escopo
- [x] Shadowing
- [ ] Operadores
- [ ] MILESTONE 01

- Aritméticos
  - multiplicador de matrizes (@)
- Lógicos
  - Operador Ternário (condicional)
- Comparativos
  - maior que >
  - menor que <
  - é igual ==
  - diferente !=
  - maior ou igual a >=
  - menor ou igual a <=
- Identidade
  - is
  - is not
- Membros
  - in
  - not in
- Bitwise
  - AND (&)
  - OR (|)
  - NOT (~)
  - XOR (^) (exclusive or)
  - RightShift (>>)
  - LeftShift (<<)
- Associativos
  - Igual =
  - Mais-Igual +=
  - Menos-Igual -=
  - Multiplicação-Igual *=
  - Divisão-Igual /=
  - Modulo-Igual %=
  - Potencia-Igual **=
  - TrueDiv-Igual //=
  - AND-Igual &= (Bitwise)
  - OR-Igual |= (Bitwise)
  - XOR-Igual ^= (Bitwise)
  - RightShift-Igual >>= (Bitwise)
  - LeftShift-Igual <<= (Bitwise)
  - Associação de expressão (Walrus Operator) :=


{se verdadeiro} if {expressão} else {se falso}

0123456789

2000

1 = 1 x 10⁰, 10 = 1 x 10¹, 100 = 1 x 10²... e por ai vai.

1 = 1 x 2⁰, 2 = 1 x 2¹, 4 = 1 x 2²... e por ai vai.

bin       dec   hex
100000 =  128 = FF

0101
1100
0100


10011100
00110100

10101000 xor

Igual =
Mais-Igual +=
Menos-Igual -=
Multiplicação-Igual *=
Divisão-Igual /=
Modulo-Igual %=
Potencia-Igual **=
TrueDiv-Igual //=
AND-Igual &= (Bitwise)
OR-Igual |= (Bitwise)
XOR-Igual ^= (Bitwise)
RightShift-Igual >>= (Bitwise)
LeftShift-Igual <<= (Bitwise)
Associação de expressão (Walrus Operator) :=

if-else

if

else

elif -> else if

while - for

while -> enquanto verdade



1. Global
2. A
3. B
4. C

Global

A {
    x = 1
    B {
        print(x)
        print(z)
        y = 2
        C {
            z = 3
        }
    }
}
A[{index inicial}:{index final+1}]
Controle de Fluxo (Control Flow) -> determina a forma como o código será executado



Sequencial: o código é executado de forma sequencial, cima a baixo

Decisivo: o código é executado baseado em uma decisão, if statements

Repetitivo: o código é executado em loop, while e for loops

Funcional: o código é dividido e executado em forma de funções (veremos mais a frente)


match-case e cadeias de elifs


if condição:
    {codigo}
else:
    {codigo}



x > 2 -> booleano: True | False


if + else -> elif





while loops

while condição:
    {codigo}

for {index} in (raio):
    {codigo}



GLOBAL

A {
    ESCOPO DE A
    x
    B {
        ESCOPO DE B
        C {
            ESCOPO DE C
            print(x)
            y
        }
    print(y)
    }



enumerate -> (posição, item)


break, continue, else

fatiar uma lista -> coletar só uma parte dela

Base: lista_resultado = ['expr_saida' for 'var' in 'iteravel']

Condicional: lista_resultado = ['expr_saida' for 'var' in 'iteravel' if (condição)]



<!-- #endregion -->
