#!/usr/bin/env python3.10
# pylint: disable=all
# region OldCode
# x, y = 2, 3
# if x == 2:
#     print(f"x é igual a {x}")
# if x != y:
#     print(f"x não é igual a y")
# nome = input("Insira seu nome: ")
# lista_amigos = ["mirai", "kaal", "beto", "kanddrex", "mine", "ramon", "zezinho", "joaquim"]
# if nome.lower() in lista_amigos:
#     print("Olá colega")
# else:
#     print("Olá estranho")
# print('''
# 1 - abrir
# 2 - ajuda
# ''')
# entrada = input("insira a resposta: ")
# if entrada == '1':
#     ...
# elif entrada == '2':
#     ...
# else:
#     exit()
# match entrada:
#     case '1':
#         ...
#     case '2':
#         ...
#     case _:
#         exit()
# pessoas = ['João', 'Mateus', 'Caio', 'Nicolas', 'Ivan']
# match pessoas:
#     case [a]:
#         print(f'Apenas um valor: {a}')
#     case [a, b]:
#         print(f'Dois itens: {a}, {b}')
#     case [a, b, c]:
#         print(f'Três itens: {a}, {b}, e {c}')
#     case [a, b, c, *rest]:
#         print(f'Mais que três itens: {a}, {b}, {c}, e também: {rest}')
#     case _:
#         print('Valor incorreto')
# action = [
#     {
#     }
# ]
# for action in actions:
#     match action:
#         case {"text": str(message), "color": str(c)}:
#             ui.set_text_color(c)
#             ui.display(message)
#         case {"sleep": float(duration)}:
#             ui.wait(duration)
#         case {"sound": str(url), "format": "ogg"}:
#             ui.play(url)
#         case {"sound": _, "format": _}:
#             warning("Unsupported audio format")
# print(True, True, True == (True, True, True))
# region Código retirado do mCoding
# Link: https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/090_match_statement_cst/cst_playground.py
#
#
# import ast
# import textwrap
# import libcst as cst
# from libcst.metadata import PositionProvider
# from libcst.tool import dump
# class Visitor(cst.CSTVisitor):
#     METADATA_DEPENDENCIES = (PositionProvider,)
#     def visit_Tuple(self, node: cst.Tuple):
#         pos = self.get_metadata(PositionProvider, node)
#         if pos.start.line != pos.end.line:
#             return
#         match node:
#             case cst.Tuple(
#                 elements=[
#                     *_,
#                     _,
#                     cst.Element(
#                         value=cst.Comparison(
#                             comparisons=[
#                                 cst.ComparisonTarget(
#                                     operator=cst.Equal(),
#                                     comparator=cst.Tuple() as tup
#                                 ),
#                             ],
#                             lpar=[],
#                             rpar=[],
#                         ),
#                     ),
#                 ],
#             ):
#                 pos = self.get_metadata(PositionProvider, tup)
#                 print(f"matched {pos.start.line, pos.start.column}")
# example_code = textwrap.dedent("""
#     a = 'hello'  # some comment
#     b="subscribe"
#     def cool(n):
#         for i in range(1, n): # hello
#             print(i * "*")
#         for i in range(n, 0, -1):
#             print(i * "*")
#         print((True, True, True == (True, True, True)))
#     True, True, (True == (True, True, True))
#     """)
# def dump_ast_example():
#     code = example_code
#     print("ORIGINAL CODE")
#     print(code)
#     node = ast.parse(code)
#     # print("ABSTRACT SYNTAX TREE")
#     # print(ast.dump(node, indent=4))
#     print("RECONSTRUCTED CODE")
#     print(ast.unparse(node))
# def dump_cst_example():
#     code = example_code
#     print("ORIGINAL CODE")
#     print(code)
#     node = cst.parse_module(code)
#     print("CONCRETE SYNTAX TREE")
#     print(dump(node, show_syntax=True, indent=" " * 4, show_whitespace=True, show_defaults=True))
#     #print("RECONSTRUCTED CODE")
#     #print(node.code)
#     #assert code == node.code  # perfect reconstruction
# def ambiguous_tuple_equality_example():
#     codes = ["True, True, True == (True, True, True)",
#              "True, True, (True == (True, True, True))",
#              "(True, True, True) == (True, True, True)", ]
#     for code in codes:
#         print(code)
#         node = cst.parse_module(code)
#         node_with_metadata = cst.MetadataWrapper(node)
#         # print(dump(node.body[0].body[0].value, show_syntax=True, indent=" " * 4, show_whitespace=True, show_defaults=True))
#         node_with_metadata.visit(Visitor())
# def main():
#     # dump_ast_example()
#     dump_cst_example()
#     #ambiguous_tuple_equality_example()
# if __name__ == '__main__':
#     main()
# variavel = ''
# if variavel:
#     print("é verdade")
# else:
#     print("é falso")
# nome = input('Insira seu nome: ')
# if nome == 'Mine':
#     print(f"'{nome}' é igual a 'Mine'")
# elif nome == 'Mirai':
#     print(f"'{nome}' é igual a 'Mirai'")
# elif nome == 'Kanddrex':
#     print(f"'{nome}' é igual a 'Kanddrex'")
# else:
#     print(f'{nome} é um estranho')
# os_malucolá = ['Mira!', 'Mirai' , 'Kaal' , 'Zezinho' , 'Ramon' ]
# nome = input('Insira seu nome: ')
# if nome == 'Mirai':
#     print("'{nome}' é igual a 'Mine'")
# else:
#     print("'{nome}' não é igual a 'Mine'")
# x = 1 #+ GLOBAL
# def A():
#     y = 5 #* ESCOPO DE A
#     print(f"ESCOPO A: {x=}")
#     print(f"ESCOPO A: {y=}")
#     print(f"ESCOPO A: {z=}")
#     def B():
#             z = 3 #! ESCOPO DE B
#             print(f"ESCOPO B: {z=}")
#         print(f"ESCOPO B: {x=}")
#         print(f"ESCOPO B: {y=}")
#     B()
# A()
# dicionario = {
#     'nome': 'Mirai',
#     'idade': 17,
#     'cor': 'azul'
# }
# match dicionario:
#     case {'nome': _, 'idade': _}:
#         print('tem nome e idade')
#     case {'nome': _, 'cor': _}:
#         print('tem nome e cor')
#     case _:
#         print('não é igual a caso nenhum')
# match action:
#     case {"text": str(message), "color": str(c)}:
#         ui.set_text_color(c)
#         ui.display(message)
#     case {"sleep": float(duration)}:
#         ui.wait(duration)
#     case {"sound": str(url), "format": "ogg"}:
#         ui.play(url)
#     case {"sound": _, "format": _}:
#         warning("Unsupported audio format")
# print('(1) - jogar')
# print('(2) - opções')
# print('(3) - ajuda')
# print('(0) - sair')
# resposta = input('> ')
# match resposta:
#     case '1':
#         jogar()
#     case '2':
#         opcoes()
#     case '3':
#         ajuda()
#     case _:
#         sair()
# if resposta == '1':
#     jogar()
# elif resposta == '2':
#     opcoes()
# elif resposta == '3':
#     ajuda()
# else:
#     sair()
# x = 3
# if x != 2:
#     print('3 é diferente de 2')
# endregion
# x = 0
# while x < 10: #? x é menor que 10?
#     print(f"valor de x: {x}")
#     x += 1 #+ x = x + 1
# for i in range(10):
#     print(i)
# lista_amigos = [
#     "Kaal",
#     "Mine",
#     "Kanddrex",
#     "Mirai",
#     "Joaquim",
# ]
# for i, v in enumerate(lista_amigos):
#     print(f"{v} está na posição {i}")
# for i in range(len(lista_amigos)):
#     print(f"{lista_amigos[i]} está na posição {i}")
# dicionario_aleatorio = {
#     "Chave A": "Valor 01",
#     "Chave B": "Valor 02",
#     "Chave C": "Valor 03",
# }
# print('CHAVES:')
# for chave in dicionario_aleatorio:
#     print(chave)
# print('VALORES:')
# for valor in dicionario_aleatorio.values():
#     print(valor)
# print('CHAVES e VALORES:')
# for chave, valor in dicionario_aleatorio.items():
#     print(chave, valor)
# lista_num1 = [1, 3, 4, 7, 9]
# lista_num2 = [1, 3, 5, 7, 9]
# print("Teste 01")
# for i in lista_num1:
#     if i % 2 == 0:
#         print("contem um numero par")
#         break
# else:
#     print("não contem um numero par")
# print("Teste 02")
# for i in lista_num2:
#     if i % 2 == 0:
#         print("contem um numero par")
#         break
# else:
#     print("não contem um numero par")
# x = 0
# while x < 10:
#     print(x)
#     x = x + 1
# lista_amigos = [
#     'Kaal',
#     'Mine',
#     'Beto',
#     'Zezinho',
#     'Kanddrex',
#     'Mirai'
# ]
# for i in lista_amigos:
#     print(i)
# x = 0
# while x < len(lista_amigos):
#     print(lista_amigos[x])
#     x += 1
# res = input("insira resposta: ")
# while res.lower() != "sair":
#     print("(1) - iniciar")
#     print("(2) - ajuda")
#     print("(3) - opcoes")
#     res = input("insira resposta: ")
# endregion
# from timeit import timeit
# def pure_while(n: int = 100000000) -> int:
#     i, x = 0, 0
#     while i < n:
#         x += i
#         i += 1
#     return x
# def pure_for(n: int = 100000000) -> int:
#     x = 0
#     for i in range(n):
#         x += i
#     return x
# print(f"While Loop:\t{timeit(pure_while, number=1)} segundos")
# print(f"For Loop:\t{timeit(pure_for, number=1)} segundos")
# x, y = [1, 2] # DESESTRUTURAÇÃO ou UNPACKING
# print(x)
# print(y)
# lista_amigos = [
#     'Kaal',
#     'Mine',
#     'Beto',
#     'Zezinho',
#     'Kanddrex',
#     'Mirai'
# ]
# for i, v in enumerate(lista_amigos):
#     print(f"O {v} está na posição {i}")
# dicionario_aleatorio = {
#     "Chave A": "Valor 01",
#     "Chave B": "Valor 02",
#     "Chave C": "Valor 03",
# }
# for k, v in dicionario_aleatorio.items():
#     print(k, v)
# for i in range(10):
#     print(i)
#     if i == 6:
#         break
# for i in range(10):
#     print(i)
#     if i == 6:
#         print("e vamos continuar")
#         continue
# for i in range(10):
#     print(i)
# else:
#     print("não tem breaks então chegamos ao fim")
# print("Teste 02")
# for i in [1, 3, 4, 7, 9]:
#     if i % 2 == 0:
#         print("contem um numero par")
#         break
# else:
#     print("não contem um numero par")
