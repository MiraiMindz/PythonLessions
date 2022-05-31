#!/usr/bin/env python3.10

# if {Condição}:
#   {Codigo}

# while {Condição}:
#   {Codigo}

# for {variavel} in {sequencia}:
#   {codigo}

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# nova_lista = [x**2 for x in nums if x %2 != 0]


# print(nums, nova_lista)

# chaves = ['a','b','c','d','e']
# valores = [1,2,3,4,5]
# dicionario = { k:v for (k,v) in zip(chaves, valores)}
# print(dicionario)

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista1[2:8])



# while True:
#     print("isso sera sempre verdade, loop infinito")



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



