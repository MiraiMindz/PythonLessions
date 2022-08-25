#!/usr/bin/env python3.10
# pylint: disable=all
# region OldCode
# AULA 01C
# CODIGO
# Nome, Idade = "Mirai", 17
# Nome3 = Nome2 = Nome    # associa Nome a Nome2 #
# PI = 3.14
# 31hh5kjheqhkjeqh
# dgkjagldkajlkgj
# print("Olá Mundo")
# print(Nome3, Nome2, Nome)
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
# print("Meu nome é %s, e eu tenho %s anos" % (nome, idade))
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
# print(f'LISTA_BASE:\t{lista_de_amigos}')
# lista_de_amigos.append('Joaquim')
# print(f'APPEND:\t\t{lista_de_amigos}')
# lista_de_amigos.insert(1, 'Mirai')
# print(f'INSERT:\t\t{lista_de_amigos}')
# ? ADICIONAR:
# * [x] list.append()
# * [x] list.insert()
# ? REMOVER:
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
# + Matrizes ou Listas Multi-dimensionais
# matriz_compras = [
# #+ X    0                       1                       2                Y
#     ['farinha de trigo',    'farinha de rosca',    'farinha de mesa'],#+ 0
#     ['queijo',              'manteiga',            'requeijão'],      #+ 1
#     ['picanha',             'linguiça',            'contra-filé']     #+ 2
# ]
# ? nome_da_matriz[Y][X]
# print(f'Antes de adicionar o Beto:\t{Alunos_de_Ciencias}')
# Alunos_de_Ciencias.add('Beto')
# print(f'Depois de adicionar o Beto:\t{Alunos_de_Ciencias}')
# print(f'Antes de remover o Mine:\t{Alunos_de_Ciencias}')
# Alunos_de_Ciencias.remove('Mine')
# print(f'Antes de remover o Mine:\t{Alunos_de_Ciencias}')
# Alunos_de_Matematica = {'Mirai', 'Luis', 'Ramon'}
# Alunos_de_Portugues  = {'Kaal', 'Ramon', 'Mine'}
# Alunos_de_Ciencias   = {'Mirai', 'Mine', 'Ramon'}
# sets_difference = Alunos_de_Matematica.difference(Alunos_de_Portugues)
# sets_symmetric_difference = Alunos_de_Matematica.symmetric_difference(Alunos_de_Portugues)
# sets_intersection = Alunos_de_Matematica.intersection(Alunos_de_Portugues)
# sets_union = Alunos_de_Matematica.union(Alunos_de_Portugues)
# print(f'Diferença entre Alunos de Matematica e Português:\n\t{sets_difference}')
# print(f'Diferença simétrica entre Alunos de Matematica e Português:\n\t{sets_symmetric_difference}')
# print(f'Interseção entre Alunos de Matematica e Português:\n\t{sets_intersection}')
# print(f'União entre Alunos de Matematica e Português:\n\t{sets_union}')
# valor1, valor2, chave1, chave2 = "valor1", "valor2", "chave1", "chave2"
# dicionario = {
#     chave1: valor1,
#     chave2: valor2
# }
# pessoa = {
#     'nome': 'Jacinto Pinto',
#     'idade': 18,
#     'profissao': 'Pedreiro',
#     'esta_desempregado': True
# }
# print(pessoa)
# print(pessoa['nome'])
# pessoa['nome'] = 'Jorge Amado'
# print(pessoa)
# print(pessoa['nome'])
# pessoa['esta_morto'] = True
# print(pessoa)
# print(pessoa['esta_morto'])
# pessoa.pop('profissao')
# print(pessoa)
# x = '3'
# print(x, type(x))
# x_int = int(x)
# print(x_int, type(x_int))
# notas = [60, 75, 40, 35, 100, 80, 90]
# media = sum(notas) / len(notas)
# print(f'{media:.2f}')
# variavel = 32
# print(variavel, hex(id(variavel)))
# variavel = 45
# print(variavel, hex(id(variavel)))
# CONSTANTE = 3.14
# print(CONSTANTE, hex(id(CONSTANTE)))
# CONSTANTE = 4
# print(CONSTANTE, hex(id(CONSTANTE)))
# resposta = input('Insira sua idade: ')
# print('sua idade é:', resposta)
# certeza = input('sua idade é 17? ')
# tem = input('tem certeza? ')
# imprimir = print
# imprimir('yee')
# string_1 = 'essa string usa aspas simples'
# string_2 = "essa string usa aspas duplas"
# print(string_1, type(string_1))
# print(string_2, type(string_2))
# citacao = "Pois então ela disse, \"Não se dirija mais a mim\"..."
# print(citacao)
# multi_line = """elas
#     preservam espaços
# e linhas"""
# print(multi_line)
# nome = 'Joaquim'
# idade = 43
# linguagem = 'Java'
# multi_fstring = f'''
# '''
# print('esse\ntexto\ntem\nvarias\nlinhas')
# print('esse\ttexto\ttem\tespaço')
# x = 0
# x += 1
# numero_1 = 3
# numero_2 = 3.0
# print(numero_1, type(numero_1))
# print(numero_2, type(numero_2))
# exemplo_1 = 8 / 4
# exemplo_2 = 1 / 3
# exemplo_3 = 8 // 4
# exemplo_4 = 1 // 3
# print(f'8 /  4:\t{exemplo_1}\t{type(exemplo_1)}\t\t(Divisão)')
# print(f'1 /  3:\t{exemplo_2:.2f}\t{type(exemplo_2)}\t\t(Divisão)')
# print(f'8 // 2:\t{exemplo_3}\t{type(exemplo_3)}\t\t(Divisão Verdadeira)')
# print(f'1 // 3:\t{exemplo_4}\t{type(exemplo_4)}\t\t(Divisão Verdadeira)')
# print(0.1 + 0.2)
# print(True  and  True)
# print(True  and  False)
# print(False and  True)
# print(False and  False)
# print(True  or True)
# print(True  or False)
# print(False or True)
# print(False or False)
# print(not False)
# print(not True)
# variavel_1 = True
# variavel_2 = False
# print(variavel_1  or  variavel_2)
# tulipa_numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(tulipa_numeros, type(tulipa_numeros))
# x, y = 1, 2
# z = x, y
# print("TUPLE:", z, "ENDEREÇO MEM:", hex(id(z)))
# z = x, y, 3
# print("TUPLE:", z, "ENDEREÇO MEM:", hex(id(z)))
# lista = [1, 2, 3]
# print("LISTA:", lista, "ENDEREÇO MEM:\t\t", hex(id(lista)))
# lista.append(4)
# print("LISTA:", lista, "ENDEREÇO MEM:\t", hex(id(lista)))
# # [ INDEX:               0         1          2          3
# # ? REVERSE-INDEX:      -4        -3         -2         -1
# lista_amigos = ["Mirai", "Beto", "Kaal", "Joaquim"]
# print(lista_amigos[-3])
# # ? ADICIONAR:
# # * [x] list.append()
# # * [x] list.insert()
# # ? REMOVER:
# #! [x] list.pop()
# #! [x] list.remove()
# lista_amigos = ["Mirai", "Beto", "Kaal", "Joaquim"]
# print(lista_amigos)
# lista_amigos.remove("Kaal")
# print(lista_amigos)
# matriz = [
#     # *X  0  1  2     Y
#     [1, 2, 3],  # * 0
#     [4, 5, 6],  # * 1
#     [7, 8, 9],  # * 2
# ]
# # *           Y  X
# print(matriz[0][2])
# Alunos_de_Ciencias = {"Mirai", "Mine", "Ramon"}
# print(f"Antes de adicionar o Beto:\t{Alunos_de_Ciencias}")
# Alunos_de_Ciencias.add("Beto")
# print(f"Depois de adicionar o Beto:\t{Alunos_de_Ciencias}")
# print(f"Antes de remover o Mine:\t{Alunos_de_Ciencias}")
# Alunos_de_Ciencias.remove("Mine")
# print(f"Antes de remover o Mine:\t{Alunos_de_Ciencias}")
# Alunos_de_Matematica = {"Mirai", "Luis", "Ramon"}
# Alunos_de_Portugues = {"Kaal", "Ramon", "Mine"}
# Alunos_de_Ciencias = {"Mirai", "Mine", "Ramon"}
# sets_difference = Alunos_de_Matematica.difference(Alunos_de_Portugues)
# sets_symmetric_difference = Alunos_de_Matematica.symmetric_difference(
#     Alunos_de_Portugues,
# )
# sets_intersection = Alunos_de_Matematica.intersection(Alunos_de_Portugues)
# sets_union = Alunos_de_Matematica.union(Alunos_de_Portugues)
# print(f"Diferença entre Alunos de Matematica e Português:\n\t{sets_difference}")
# print(
#     f"Diferença simétrica entre Alunos de Matematica e Português:\n\t{sets_symmetric_difference}",
# )
# print(f"Interseção entre Alunos de Matematica e Português:\n\t{sets_intersection}")
# print(f"União entre Alunos de Matematica e Português:\n\t{sets_union}")
# valor1, valor2, chave1, chave2 = "valor1", "valor2", "chave1", "chave2"
# dicionario = {
#     chave1: valor1,
#     chave2: valor2,
# }
# dicionario["chave3"] = "valor3"
# dicionario["chave2"] = "carro"
# dicionario.pop("chave2")
# print(dicionario)
# x = 3
# print(x, type(x))
# y = str(x)  # converte 3 int em "3" string
# print(y, type(y))
# notas = [9.4, 9.0]
# soma = sum(notas)
# comprimento = len(notas)
# media = soma / comprimento
# print(media)
# x = oct(18)
# print(x)
# estudantes_portugues = {'Mine', 'Kanddrex', 'Kaal', 'Joaquim'}
# estudantes_matematica = {'1', '2', '3', '4'}
# print(estudantes_matematica)
# Alunos_de_Ciencias = {"Mirai", "Mine", "Ramon"}
# print(f"Antes de adicionar o Beto:\t{Alunos_de_Ciencias}")
# Alunos_de_Ciencias.add("Beto") #+ AQUI A GENTE ADICIONA O BETO
# print(f"Depois de adicionar o Beto:\t{Alunos_de_Ciencias}")
# print(f"Antes de remover o Mine:\t{Alunos_de_Ciencias}")
# Alunos_de_Ciencias.remove("Mine") #+ AQUI A GENTE REMOVE O MINE
# print(f"Antes de remover o Mine:\t{Alunos_de_Ciencias}")
# Alunos_de_Matematica = {"Mirai", "Luis", "Ramon"}
# Alunos_de_Portugues = {"Kaal", "Ramon", "Mine"}
# sets_difference = Alunos_de_Matematica.difference(Alunos_de_Portugues)
# sets_symmetric_difference = Alunos_de_Matematica.symmetric_difference(Alunos_de_Portugues)
# sets_intersection = Alunos_de_Matematica.intersection(Alunos_de_Portugues)
# sets_union = Alunos_de_Matematica.union(Alunos_de_Portugues)
# print(f"Diferença entre Alunos de Matematica e Português:\n\t{sets_difference}")
# print(f"Diferença simétrica entre Alunos de Matematica e Português:\n\t{sets_symmetric_difference}")
# print(f"Interseção entre Alunos de Matematica e Português:\n\t{sets_intersection}")
# print(f"União entre Alunos de Matematica e Português:\n\t{sets_union}")
# pessoa = {
#     'nome': 'Joaquim Souza',
#     'idade': 18,
#     'profissao': 'Pedreiro',
# }
# print(pessoa)
# pessoa.pop
# print(pessoa)
# numero = 0
# conversao = bool(numero)
# print(numero, type(numero))
# print(conversao, type(conversao))
# notas = [80, 90, 100, 100]
# print(notas)
# soma = sum(notas)
# comprimento = len(notas)
# media = soma / comprimento
# print(media)
# print()
# palavra = "nan"
# x = float(palavra)
# print(x)
# endregion
# nome = 'Mirai'
# idade = 17
# fString  =  f'meu nome é {nome} e eu tenho {idade}, nasci em {2022 - idade}' #+ Formated String
# rString  =  r'essa string tem \ntabs e \t\tnewlines' #+ Raw String
# uString  =  u'Runic Ansus: \u16A8' #+ Unicode String
# rfString = rf'meu nome:\t{nome}' #+ Raw-Formated String
# print(fString)
# print(rString)
# print(uString)
# print(rfString)
# from string import Template
# template_string = Template("Olá meu nome é $nome, e eu estou ${acao}ndo")
# print(template_string.substitute(nome="Joaquim", acao="Programa"))
# carro = "Runic Ior: ᛡ"
# print(f'{carro=}')
# nome = 42 / 88
# print(f'{nome:.2%}')
# nome = 'Mirai'
# idade = 17
# print('meu nome é %s e eu tenho %d anos' % (nome, idade))
