#!/usr/bin/env python3.10

# DESAFIO:
# escrever um programa que pega uma lista de numeros, e retorna a media deles


# region TIPOS BASICOS
# Primitivos:
#   Strings (Textos):
# ''
# ""

#   Integers & Floats (Numeros Inteiros e Numeros de Ponto Flutuante):
# 1997
# 3.1415 # o . -> Padrão Americano

# + -> soma
# - -> subtração
# ** -> potencia
# * -> mutiplicação
# / -> divisão
# // -> "divisão verdadeira"
# % -> modulo

# media = 567 + 890 + 1000 + 321 + 700
# print(media)
# print("{:.2f}".format((media/6)/100))

# PYTHON:
#   1 - ((((())))) -> DE DENTRO PRA FORA
#   2 - POTENCIA
#   3 - RAIZES
#   4 - MUTIPLICAÇÃO
#   5 - DIVISÃO
#   6 - SOMA
#   7 - SUBTRAÇÃO

#   Boolean (Booleano):
# True    # Verdadeiro | Verdade
# False   # Falso

# and -> COMBINA
# or -> SE 1 FOR VERDADE
# not -> INVERTE2

# print(True and True) # -> Verdade
# print(True and False) # -> Falso
# print(False and True) # -> Falso
# print(False and False) # -> Falso

# print(True or True) # -> Verdade
# print(True or False) # -> Verdade
# print(False or True) # -> Verdade
# print(False or False) # -> Falso

#print(not True)

# variavel1 = False
# variavel2 = True

# print(variavel2 and variavel1)


# nome = "Mirai" # <- 1 TEXTO, 1 DADO, 1 INFORMAÇÂO

# idade = 17 # <- 1 NUMERO, 1 DADO, 1 INFORMAÇÂO
# endregion

# region TIPOS COMPLEXO
# Compostos:
#   LISTAS
#   DICIONARIO
#   TUPLES (TULIPA)
#   SET (CONJUNTO)

# endregion

#region DUMP
# nome = "mirai"
# idade = 17
# local = "discord"
# materia = "PYTHON"

# #print("Meu nome é " + nome + " eu tenho " + str(idade) + " dou aula no " + local + " sobre a linguagem " + materia)

# #print("meu nome é {}".format(nome))
# print(f"Meu nome é {nome.capitalize()} eu tenho {idade} dou aula no {local.upper()} sobre a linguagem {materia.lower()}")

# input()
# print()
# str()
# int()
# bool()
# float()


# Desafio:
#   escreva um pequeno programa que pega informações do Usuário e faz algumas ações
# como operações matematicas
# concatenações
# formatação
# prints
# conversões

#           0           1             2           3
# nomes = ['Mirai',   'Kanddrex',     'Mine',     'Kaal']
# print(nomes[0])

#region DESAFIO:

################################################################
# Escrever um programa que mostra a lista de amigos do usuário #
# e permite que ele adicione novos amigos e veja a nova lista  #
#                                                              #
#   - Lista                                                    #
#   - input()                                                  #
#   - print()                                                  #
#                                                              #
#   - VER a Lista                                              #
#   - ADICIONAR Amigos                                         #
#                                                              #
#   COISAS QUE VOCE AINDA VAI APRENDER:                        #
#       - switch-case                                          #
#       - while                                                #
#                                                              #
################################################################

# def menu_updt(op:str):
#     print(op)
#     return int(input("Insira sua resposta numerica: "))


# lista_amigos = []
# opcoes = """\t- 1: VER LISTA
# \t- 2: ADICIONAR AMIGOS
# \t- 0: SAIR"""
# tela_inicial = f"""bem vindo ao programa de amizadas, o que desejas fazer?
# {opcoes}"""

# print(tela_inicial)
# resposta = int(input("Insira sua resposta numerica: "))
# while resposta != 0:
#     match resposta:
#         case 1:
#             print(lista_amigos)
#             resposta = menu_updt(opcoes)
#         case 2:
#             amigo_adicionar = input("Insira o nome do amigo a ser adicionado: ").capitalize()
#             lista_amigos.append(amigo_adicionar)
#             print("Amigo adicionado")
#             resposta = menu_updt(opcoes)
#         case 0:
#             break
#         case _:
#             resposta = menu_updt("Não entendi, poderia repetir?")

#region CODIGO_FINAL:

# lista_opc = """\t- 1: VER LISTA DE AMIGOS
# \t- 2: ADICIONAR AMIGO A LISTA
# \t- 0: SAIR"""

# mensagem_inicial = f"""Olá, seja bem-vindo ao programa de amigos, favor digitar numero do que desejas fazer:
# {lista_opc}
# """
# print(mensagem_inicial)
# resposta = input("Insira sua resposta: ")
# lista_amigos = []


# while resposta != 0:
#     match int(resposta):
#         case 1:
#             print(lista_amigos)
#             print(lista_opc)
#             resposta = input("Insira sua resposta: ")
#         case 2:
#             amigo_add = input("Insira o nome do amigo a ser adicionado: ").capitalize()
#             lista_amigos.append(amigo_add)
#             print(lista_opc)
#             resposta = input("Insira sua resposta: ")
#         case 0:
#             break
#         case _:
#             print("Desculpe, o que quiz dizer?")
#             print(lista_opc)
#             resposta = input("Insira sua resposta: ")

#endregion

#endregion

# Index

# amigos_internet = ['Mirai', 'Kanddrex', 'Mine', 'Kaal']
# amigos_pessoais = [
#     'Ana',
#     'Vlad',
#     'Caua',
#     'Bruno',
#     'Pedro'
#     ]

# print(f"Amigos antes do Hyakk: {amigos_internet}")
# amigos_internet.append('Hyakk')
# print(f"Amigos depois do Hyakk: {amigos_internet}")
# amigos_internet.append(amigos_pessoais)
# print("APPEND amigos_pessoais: ", amigos_internet)

# amigos_internet.remove('Mine')
# print("REMOVE 'Mine': ", amigos_internet)
# amigos_internet.pop()
# print("POP: ", amigos_internet)
# amigos_internet.pop()
# print("POP: ", amigos_internet)
# amigos_internet.join()

# matriz = [
# #     0   1   2
#     ['A','B','C'], # 0
#     ['D','E','F'], # 1
#     ['G','H','J']  # 2
# ]

# #            X  Y
# print(matriz[1][2])
# # X = Index da Lista
# # Y = Index do Valor

# x, y = 1, 2
# # (x, y) = (1, 2)

# z = 7

# tulipa_nova = x, + y, + z
# print(tulipa_nova)

# alunos_matematica = {'Kanddrex', 'Mine', 'Mirai', 'Kaal'}
# alunos_portugues = {'Shiwa', 'Kaal', 'Mine', 'Pedrin'}

# print(alunos_matematica.intersection(alunos_portugues))
# print(alunos_matematica.union(alunos_portugues))
# print(alunos_portugues)

# CHAVE=VALOR

# lista_amigos = ['Mirai', 'Mine', 'Kanddrex']
# lista_idades = [17, 13, 16]

# dicionario_amigos_idade = {
#     'Mirai': 17,
#     'Mine': 13,
#     'Kanddrex': 16
# }

# print(dicionario_amigos_idade['Mine'])

# dicionario_amigos_idade['Pedrinho'] = 18

# print(dicionario_amigos_idade)

# dicionario_amigos_idade.update({'Pedrinho': 18})

# endregion

#print(bin(200))

# 2^n - 1

#  2³     2²     2¹   2⁰ - 1
# [4]   [3]   [2]   [1]
#  0     0    0      0
#  8     4    2      1
# --------------------
# 0      0    1      0 = 0010 = 2
# 0      1    0      0 = 0100 = 4
# 0      1    0      1 = 101 = 5

#print(bin(5))

# print(complex(2))
