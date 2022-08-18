#!/usr/bin/env python3.10

#region OldCode
# AULA 01C

# CODIGO

#Nome, Idade = "Mirai", 17
#Nome3 = Nome2 = Nome    # associa Nome a Nome2 #

#PI = 3.14

# 31hh5kjheqhkjeqh
# dgkjagldkajlkgj

#print("Olá Mundo")
#print(Nome3, Nome2, Nome)

# prompt = "Insira algo -> "

# texto = input(prompt)
# print("voce disse:", texto)

# imprimir = print

# imprimir("eu disse algo")
# '((()))'

# exit()

#

# AULA 02A

# nome = "Mirai"
# linguagem = 'Python'

# print(nome, linguagem)

# ingles = "Hi my name is Mirai and I'm a programmer."
# portugues = 'E então ele disse: "não venha mais a mim."'

# ingles2 = 'Hi my name is Mirai and I\'m a programmer.'

# tab = "esse\ttexto\ttem\ttab"

# print(tab)

# newline = "esse\ntexto\ntem\nnovas\nlinha"

# print(newline)

# retrn1 = "Um\bTexto\bQualquer\b"

# print(retrn1)

# multi = '''ela é uma string

# que preserva muito bem

#     \todos os espaços
# '''

# print(multi)


# nome = "Mirai"
# idade = 17
# linguagem = "Python"

# string = str()


# print("Olá meu nome é " + nome + " eu tenho " + str(idade) + " anos e programo em " + linguagem)

# print("Olá meu nome é {} eu tenho {} anos e programo em {}".format(nome, idade, linguagem))

# print(f"Olá meu nome é {nome} eu tenho {idade} anos e programo em {linguagem}")

# print(f'''Olá meu nome é


# {nome} eu tenho


# {idade} anos e programo em {linguagem}
# ''')


#print("Meu nome é %s, e eu tenho %s anos" % (nome, idade))

# AULA 02B

# AULA 03C

# print(6.5 + 3.7)
# print((65 + 37)/10)

#       BASE      OPERADOR    EXPOENTE
# print(3            **              2)
# print(type(True))
# print(type(False))

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not False)


# A = True
# B = False

# print(B and A)
# print(A or B)

# comp_num = 100_000_000


# x = [1, 2, 3, 4]
# print("TIPO:",x,"ENDEREÇO MEM:", hex(id(x)))
# x.append(5)
# print("TIPO:", x,"ENDEREÇO MEM:", hex(id(x)))


# x, y = 1, 2
# z = x, y
# print("TIPO:", z, "ENDEREÇO MEM:", hex(id(z)))
# z = x, y, 3
# print("TIPO:", z, "ENDEREÇO MEM:", hex(id(z)))


# x, y = 1, 2 #! EXCETO DECLARAÇÂO DE MULTIPLAS VARIAVEIS

# # print(x)
# # print(y)

# cParent = (
#     1,
#     2,
#     3,
#     4
# )



# print(cParent)

# sParent = 'a', 'b', 'c', 'd'
# print(sParent, type(sParent))

# tuple = ('a', 3, True, (1, 2, 3))
# print(tuple)

# AULA 04B

# idade = 17
# nome = 'Mirai'

# template_string = f'Olá meu nome é {nome} e eu tenho {idade} anos'

# # print(template_string)


# multiline_fstring = f"""

# """

# texto = "Meu nome é %s e eu tenho %05d"

# print(texto % (nome, idade))

# x, y = 1, 2
# tulipa = x, y
# print("VARIAVEL:", tulipa, "\tENDEREÇO MEM:", hex(id(tulipa)))
# tulipa = x, y, 3
# print("VARIAVEL:", tulipa, "\tENDEREÇO MEM:", hex(id(tulipa)))

#endregion


# print(f'LISTA_BASE:\t{lista_de_amigos}')

# lista_de_amigos.append('Joaquim')
# print(f'APPEND:\t\t{lista_de_amigos}')

# lista_de_amigos.insert(1, 'Mirai')

# print(f'INSERT:\t\t{lista_de_amigos}')

#? ADICIONAR:
#* [x] list.append()
#* [x] list.insert()
#? REMOVER:
#! [x] list.pop()
#! [x] list.remove()

# #[ INDEX:            0       1          2          3
# #? REVERSE-INDEX:   -4      -3         -2         -1
# lista_de_amigos = ['Kaal', 'Mine', 'Kannddrex', 'Ramon']

# # lista_de_amigos.pop()
# # print(f'POP ULTIMO:\t\t{lista_de_amigos}')
# # lista_de_amigos.pop(1)
# # print(f'POP INDEX:\t\t{lista_de_amigos}')

# lista_de_amigos.remove('Mine')
# print(f'POP REMOVE \'Mine\':\t{lista_de_amigos}')

#+ Matrizes ou Listas Multi-dimensionais


matriz_compras = [
#+ X    0                       1                       2                Y
    ['farinha de trigo',    'farinha de rosca',    'farinha de mesa'],#+ 0
    ['queijo',              'manteiga',            'requeijão'],      #+ 1
    ['picanha',             'linguiça',            'contra-filé']     #+ 2
]


#? nome_da_matriz[Y][X]
