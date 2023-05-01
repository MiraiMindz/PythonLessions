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

Sequencial
x = 4
y = x + 2
print(y)

Decisivo
x > 4
x < 4?

se x == 4 {
    dkasd
} se não {
    adfdafj
}

Repetitivo

x = 0
enquanto x < 20 {
    x += 1
}





if (decisão):
    codigo

else + if


Cadeia de elif

(elif-chain)


comparação de padrão estrutural

[
    {}, {}, {}
]

[
    [],[],
]


match pessoas:
	case [a]:
		print(f'Apenas um valor: {a}')
	case [a, (b,)]:
		print(f'Dois itens: {a}, {b}')
	case [a, b, c]:
		print(f'Três itens: {a}, {b}, e {c}')
	case [a, b, c, *rest]:
		print(f'Mais que três itens: {a}, {b}, {c}, e também: {rest}')
	case _:
		print('Valor incorreto')


if len(pessoas) == 2 and type(pessoas[1]) == type(())







enquanto ALGO_FOR_VERDADE {
    exec codigo
}



FOR -> while com condição



delimitador de localidade



<!-- Global

importante = 3

A {
    x = 5
    B {
        y = "cachorro"
        print(x)
        C {
            nonlocal x = 3
            print(x)
            
            D {
                importante = 8
                print(x)
                print(y)
            }

            print(y)
        }

        print(x)
    }
    print(x)
} -->

0 - 30

se for divisivel por 3, exibe "Fizz"
se for divisivel por 5, exibe "Buzz"
se for divisivel por 3 e 5, exibe "FizzBuzz"
se não for, exibe o numero


1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz


Compreensão
    - Lista
    - Set
    - Dicionário
    é gerar um tipo de dado composto de forma dinamica

Expressões:
lista: ``lista_resultado = ['expr_saida' for 'var' in 'iteravel']`







Funções

é um parte de código independente que pode ser re-utilizada, elas servem para exercer uma FUNÇÃO (vide o nome).


def nome_da_funcao():
    corpo_da_função

Argumentos e Parametros

Args && Kwargs

* **


{
    "permission": valor
    ...

    800
}

for dict.Keys()
    x = {}

    **x









lambda {argumentos} : {expressão}



Função anonima

- Uso Unico
- Sem declaração



Função de Primeira Classe

Função de Alta Ordem

Conceitos da programação funcional

------


Função de Primeira Classe



key indentificador() {
    codigo
}

tipo identificador = valor

variavel do tipo `function` -> Callable


------

Função de Alta Ordem

Retornam uma função

*Uma função que gera uma função*



global

nonlocal





IDEAL até 3 niveis de identação





- Aritmeticos
- Logicos
- Comparativos
- Bitwise
- Associativos
- Identidade
- Membros



+
-
*
/
**
//
%
@ 




>
<
==
!=
>=
>=


is

is not

in

not in







AND (&)
OR (|)
NOT (~)
XOR (^) (exclusive or)
RightShift (>>)
LeftShift (<<)





1 = 1 x 10^0
50 = 5 x 10^1
600 = 6 x 10^2


505

13 10 + 3

1 x 10^1 + 3 x 10^0 = 13

10 + 3


0 -> 0
1 -> 1

2^n - 1, sendo o numero de bits

2^7 2^6 2^5 2^4 2^3 2^2 2^1  2^0





128  64  32  16  8   4   2   1
[0] [0] [0] [1] [0] [1] [0] [1]

2^2 + 2^0
4 + 1 = 5