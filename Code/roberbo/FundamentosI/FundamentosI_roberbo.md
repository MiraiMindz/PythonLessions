mais usados
variaveis, comentarios, print() e imput()

a = 1
b = 2
ou
a, b = 1, 2 (nessa ordem)

comentarios: não executa oque esta em comentario ou em #

print:mostra texto no terminal

input: congela para que possa inserido algo

input entrada, print saida

fundamentos p2

dado: e tudo aquilo que guarda informação 

tipos de dado: primitivo e composto

primitivo: guarda apenas uma informação ou um dado
string(str)
concatenação -> juntar dois textos
integers e floats (int e float)
booleans (bool)

verdadeiro:
-string não vazia
-numero diferente de 0
-dados que não estejam vazio

falsos:
-strings vazias (""ou'')
-0
-qualquer tipo de dado vazio

operadores lógicos
-and: se todos forem True da True e se um for False ele da False
-or:ao contrario do and
-not: inverte True pelo False e False pelo True

curiosidades:

floats(nan - inf)

strings(prefixos sequencia de escapagem tamplate convertores mini linguagem depuração e padrao printf)

prefixos:
r ou R raw strings (rstring)
u ou U unicode strings (ustring)
f ou F format string (fstring)
fr ou FR ou fR ou Fr ou rF ou Rf ou RF raw format strings (frstring ou rfstring)

sequencia de escapagem
\t = \tab \n = \nova linha \' \""

tamplate

convertores
!A: representação ASCII
!R: o equivalente a repr()
!S: o equivalente a str()

a mini linguagem

especificação   ::=  [[preenchimento]alinhamento][sinal][#][0][largura][agrupamento][.precisão][tipo]
preenchimento   ::=  <qualquer caractere>
alinhamento     ::=  "<" | ">" | "=" | "^"
sinal           ::=  "+" | "-" | " "
largura         ::=  digito+
agrupamento     ::=  "_" | ","
precisão        ::=  digito+
tipo            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

depuração 

padrao printf

coisa de veio


nan - recebe quando faz algo que não é um numero

inf - postivio ou neg


composto: guarda varios tipos de informação ou varios dados

tuples
listas
sets
dicionarios