# TEXTO

<!--#region OldCode -->
## AULA 01C
Variaveis, Comentários, print() e input()

Dinamicamente tipada?


Variavel -> pode variar
Constante -> nao muda

SheBang
****

## AULA 02A

TIPOS - PRIMITIVOS

Node -> informação



SIMPLES -> COMPOSTOS

SIMPLES (4):
    - String
    - Integros e Floats (Numeros)
    - Booleano


String = Texto

multi-line string


"Olá meu nome é Joaquim  eu tenho 17 anos e programo em Python"

"Olá meu nome é {Nome} eu tenho {idade} anos e programo em {Linguagem}"


			   CASA 1		CASA 2				  CASA 3	   PESS 1	 PESS 2		PESS 3
"Olá meu nome é { } eu tenho { } anos e programo em { }".format(idade	,nome , 	linguagem)

## AULA 02B

## AULA 03C

int -> 300 12
float -> 3.14

float_num = 10.

10 -> endereço
23456 -> outro endereço

\+ -> soma
\- -> subtração
\** -> potencia
\* -> mutiplicação
/ -> divisão
// -> "divisão verdadeira"
% -> modulo :: Resto da divisão


BOOLEANO - Bool - Boolean - Conjunto de logica combinatoria

2 - Verdadeiro ou Falso

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

Operadores Lógicos 3
AND
OR
NOT


Curto Circuito - Diminuir o tempo em uma decisão

# AULA 04A

TC = Tipo Composto
TC é qualquer tipo que tem mais de 1 Dado

4 Tipos Compostos:
 - Tuples (Tulipas)
 - Listas
 - Sets
 - Dicionarios

Mutabilidade: capacidade de um tipo ser alterado sem criar um novo.

IMUTAVEIS

2 modos de declaração

()

,

DADOS HOMOGENEOS


# AULA 04B



Olá meu nome é {NOME} e eu tenho {IDADE} anos

fString

Estilo de formatação printF

 - 'd' Signed integer decimal.
 - 'i' Signed integer decimal.
 - 'o' Signed octal value.
 - 'u' Obsolete type – it is identical to 'd'.
 - 'x' Signed hexadecimal (lowercase).
 - 'X' Signed hexadecimal (uppercase).
 - 'e' Floating point exponential format (lowercase).
 - 'E' Floating point exponential format (uppercase).
 - 'f' Floating point decimal format.
 - 'F' Floating point decimal format.
 - 'g' Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
 - 'G' Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
 - 'c' Single character (accepts integer or single character string).
 - 'r' String (converts any Python object using repr()).
 - 's' String (converts any Python object using str()).
 - 'a' String (converts any Python object using ascii()).
 - '%' No argument is converted, results in a '%' character in the result.

'#' The value conversion will use the “alternate form” (where defined below).
'0' The conversion will be zero padded for numeric values.
'-' The converted value is left adjusted (overrides the '0' conversion if both are given).
' ' (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
'+' A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).

4 Tipos Compostos:
 - Tuples (Tulipas)
 - Listas
 - Sets
 - Dicionarios

MUTABILIDADE

# AULA 05C

As Listas são mutaveis, então eu posso adicionar elementos

INDEX

uma matriz essencialmente é uma lista de listas

Sets -> Conjuntos

Alunos de Matematica
Alunos de Portugues
Alunos de Ciencias

Conversão | Coerção

Conversão -> EXPLICITA
Coerção -> IMPLICITA



str()   -> converte para string
int()   -> converte para int
float() -> converte para float
bool()  -> converte para booleano
tuple() -> converte para tuple
list()  -> converte para lista
set()   -> converte para set
dict()  -> converte para dicionario

Variaveis, comentarios, input() e print()

print -> exibe

SheBang

input() -> coleta

Tipos de Dado:

Eles são divididos entre Primitivos (ou Simples, ou Básicos) e Compostos (ou Agrupados, ou Complexos)

Dados Simples:

- Strings (Texto)
  - [x] - declaração
  - [x] - multi-line
  - [x] - format
- Ints & Floats (Numeros)
- Booleano (Verdadeiro e Falso)

fString

Int -> Numero Inteiro
Float -> Numero decimal

+ -> soma
- -> subtração
** -> potencia
* -> mutiplicação
/ -> divisão
// -> "divisão verdadeira"
% -> modulo

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

and, or, not

Tipos Compostos:
- Tuples
- Listas
- Sets
- Dicionarios

Mutabilidade: define a capacidade de um tipo ser alterado sem que se seja criado um novo.

CHAVE:VALOR

str() -> converte para string
int() -> converte para int
float() -> converte para float
bool() -> converte para booleano
tuple() -> converte para tuple
list() -> converte para lista
set() -> converte para set
dict() -> converte para dicionario

sum() & len()

bin() & complex()

- [x] Sets (Conjuntos)
- [x] Dicionarios
- [x] Conversão e Coerção
- [x] sum() e len()
- [x] Strings EXTRA


1. Eles não tem ordem
2. Eles não tem elemento repetido


set.add() -> adiciona elementos ao set
set.remove() -> remove elementos do set
set.difference() -> retorna a diferença entre sets
set.symmetric_difference() -> retorna todos os itens que não estão na interseção
set.intersection() -> retorna a intersceção dos sets
set.union() -> retorna a união dos sets


listas `chave:valor`


str() -> converte para string
int() -> converte para int
float() -> converte para float
bool() -> converte para booleano
tuple() -> converte para tuple
list() -> converte para lista
set() -> converte para set
dict() -> converte para dicionario

\	  Backslash ()
'	  Aspas simples (')
"	  Aspas duplas (")
\a	Sino ASCII (BEL)
\b	Backspace ASCII (BS) (apagar)
\f	Formfeed ASCII (FF)
\n	Linefeed ASCII (LF) (nova linha)
\r	Carriage Return ASCII (CR) (enter)
\t	Tab Horizontal ASCII (TAB)
\v	Tab Vertical ASCII (VT)
\ooo	Caractere com o valor octal OOO
\xhh	Caractere com o valor hexadecimal HH
\uXXXX	Caractere Unicode com o valor XXXX



Sinal	Significado
>	define que o campo deve estar alinhado a esquerda do espaço provido
<	define que o campo deve estar alinhado a direita do espaço provido
=	define que o alinhamento deve estar entre o sinal (se houver) e o digito, essa opção de alinhamento só é valida para tipos numericos
^	define que o campo deve estar alinhado ao centro do espaço provido

Variaveis, Comentários, print() e input()

constante = nao muda
variavel = muda

SheBang -> Sistemas UNIX (Linux, MacOS, FreeBSD)

print -> exibe
input -> coleta

Tipos de Dado:

Dado é tudo que guarda informação, ela pode ou não fazer sentido.

Eles são divididos entre:
Primitivos (ou Simples, ou Básicos)
Compostos (ou Agrupados, ou Complexos)

(Jargões)

Primitivos -> Guardam apenas uma informação, 3 categorias, 4 tipos.
- String (str) -> Texto
- Booleano (bool) -> Verdadeiro ou Falso
- Numericos (int & float) -> Inteiros e Decimais

str -> qualquer texto

\ -> caractere de escapagem

Multi-line String

Olá, meu nome é Mirai, eu tenho 17 anos e sei programar em Python

contatenação é o ato de juntar duas strings

format

fString -> formatted-string

2 tipos numeros:
- Ints -> Inteiros
- Floats -> Decimais

float -> floating point numbers -> numeros de ponto flutuante

+ -> soma
- -> subtração
** -> potencia
* -> mutiplicação
/ -> divisão
// -> "divisão verdadeira"
% -> modulo

1 - Parenteses () -> em sequencia, ou seja, externos primeiro
2 - Exponenciação, -> **
4 - Mutilicativos, -> *, @
5 - Divisivos, -> /, // e %
6 - Adição -> +
7 - Subtração -> -


a divisão SEMPRE retorna um float, mesmo com o resultado sendo inteiro.

a "divisão verdadeira", retorna um int.

Modulo -> resto da divisão



perfomance - bit-overflow


booleano é Verdadeiro ou Falso

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


and, or, not


"NaN" -> Not A Number
"inf"

- [x] Prefixos
- [x] Sequencias de escapagem
- [x] Templates
- [x] Conversores
- [x] Especificações da Mini-linguagem de formatação
- [x] Depuração e padrão printf


r ou R -> raw strings (rString)
u ou U -> unicode strings (uString)
f ou F -> format strings (fString)

fr ou Fr ou fR ou FR ou rf ou rF ou Rf ou RF -> raw-format strings (frString ou rfString)


\\	Backslash (\\)
'	Aspas simples (')
"	Aspas duplas (")
\a	Sino ASCII (BEL)
\b	Backspace ASCII (BS) (apagar)
\f	Formfeed ASCII (FF)
\n	Linefeed ASCII (LF) (nova linha)
\r	Carriage Return ASCII (CR) (enter)
\t	Tab Horizontal ASCII (TAB)
\v	Tab Vertical ASCII (VT)
\ooo	Caractere com o valor octal OOO
\xhh	Caractere com o valor hexadecimal HH
\uXXXX	Caractere Unicode com o valor XXXX


!a -> Representação ascii
!r -> o equivalente a repr()
!s -> o equivalente a str()

especificação   ::=  [[preenchimento]alinhamento][sinal][#][0][largura][agrupamento][.precisão][tipo]
preenchimento   ::=  <any character>
alinhamento     ::=  "<" | ">" | "=" | "^"
sinal           ::=  "+" | "-" | " "
largura         ::=  digit+
agrupamento     ::=  "_" | ","
precisão        ::=  digit+
tipo            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

%d	Numero inteiro com sinal
%i	Numero inteiro com sinal
%o	Numero octal com sinal
%u	OBSOLETO, equivalente a %d
%x	Numero hexadecimal minusculo com sinal
%X	Numero hexadecimal maiusculo com sinal
%e	expoente minusculo
%E	expoente maiusculo
%f e %F	precisão de ponto flutuante
%g	precisão de ponto flutuante. Usa notação exponecial minuscula caso o expoente é menor que -4, caso contrario usa o formado decimal.
%G	precisão de ponto flutuante. Usa notação exponecial maiuscula caso o expoente é menor que -4, caso contrario usa o formado decimal.
%c	converte para um caractere
%r	converte para o equivalente ao repr()
%s	converte para o equivalente ao str()
%a	converte para o equivalente ao ascii()
%%	uma % (porcentagem)

Tipo Compostos
- [x] Tuples
- [x] Listas
- [x] Sets
- [x] Dicionarios

Mutabilidade -> a capacidade de um tipo, ser alterado, sem criar um novo.

As tuples (tulipas), são imutaveis.

()
,

Matrizes (Lista Multi-Dimensional)



Set -> Conjunto


eles não tem ordem
eles não tem valor repetido.

lista chave:valor


Conversão & Coerção, `sum()` & `len()`

str()   -> converte para string
int()   -> converte para int
float() -> converte para float
bool()  -> converte para booleano
tuple() -> converte para tuple
list()  -> converte para lista
set()   -> converte para set
dict()  -> converte para dicionario

Variaveis, Comentários, print() e input()

Tipos de Dado

Dado é tudo aquilo que guarda informação, ou seja, um numero, um texto, Verdadeiro ou Falso, uma letra, qualquer coisa que seja informação

Primitivos (ou Simples, ou Básicos)
- Strings (str)
CONCATENAÇÃO -> Juntar dois textos

- Integers e Floats (int & float)

soma: +
subtração: -
potencia: **
mutiplicação: *
divisão: /
"divisão verdadeira": //
módulo: %

- Booleans (bool)

Verdadeiros:
- True
- Qualquer string que não esteja vazia
- Qualquer numero diferente de 0
- Qualquer outro tipo de dado que não esteja vazio

Falsos:
- False
- Strings vazias ("" ou '')
- 0
- Qualquer outro tipo de dado vazio

Operadores Lógicos
- and
- or
- not




NaN - inf

Prefixos
Sequencias de escapagem
Templates
Conversores
Especificações da Mini-linguagem de formatação
Depuração e padrão printf



Prefixos:
  r ou R: raw strings (rString)
  u ou U: unicode strings (uString)
  f ou F: format strings (fString)

  fr ou Fr ou fR ou FR ou rf ou rF ou Rf ou RF: raw-format strings (frString ou rfString)


    !a: Representação ASCII
    !r: o equivalente a repr()
    !s:o equivalente a str()




Especificações da Mini-linguagem de formatação


especificação   ::=  [[preenchimento]alinhamento][sinal][#][0][largura][agrupamento][.precisão][tipo]
preenchimento   ::=  <qualquer caractere>
alinhamento     ::=  "<" | ">" | "=" | "^"
sinal           ::=  "+" | "-" | " "
largura         ::=  digito+
agrupamento     ::=  "_" | ","
precisão        ::=  digito+
tipo            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


Depuração e padrão printf


Compostos (ou Agrupados, ou Complexos)


Tuples
Listas
Sets
Dicionarios = {
  "chave": valor,
}

media = sum(Dicionarios["chave"]) / len()



str(): converte para string
int(): converte para int
float(): converte para float
bool(): converte para booleano
tuple(): converte para tuple
list(): converte para lista
set(): converte para set
dict(): converte para dicionario

coerção

<!-- #endregion -->

