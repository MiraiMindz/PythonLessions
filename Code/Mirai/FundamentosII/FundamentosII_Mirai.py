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
# #?   -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
# #+     0,  1,  2,  3,  4,  5,  6,  7,  8,  9
# A = [  1,  5,  4,  2,  3,  7,  0,  8,  6,  9]
# #*                     3   7   0
# print(A[2:])
# lista_dobrada = []
# for i in range(1, 11):
#     lista_dobrada.append(i * 2)
# print(lista_dobrada)
# lista_dobrada = [i * 2 for i in range(1, 11)]
# print(lista_dobrada)
# lista_de_pares = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         lista_de_pares.append(i)
# print(lista_de_pares)
# lista_de_pares = [i for i in range(1, 11) if i % 2 == 0]
# print(lista_de_pares)
# adicione 'i' para a lista 'lista_de_pares' caso o resto da divisão(modulo) por 2 for igual a 0 em um raio entre 1 e 11
# set_de_pares = {i for i in range(1, 11) if i % 2 == 0}
# print(set_de_pares)
# res_dict = {}
# for i in range(1, 10):
#     if i % 2 != 0:
#         res_dict[i] = i**3
# print(res_dict)
# comp_dict = {i: i**3 for i in range(1, 10) if i % 2 != 0}
# print(comp_dict)
# lista_nums = [1, 2, 3, 4, 5]
# lista_chars = ["a", "b", "c", "d", "e"]
# zip_dict = {k:v for (k, v) in zip(lista_nums, lista_chars)}
# print(zip_dict)
# def apresentar(): #+ DECLAREI
#     print("olá meu nome é Mirai")
# apresentar()    #+ CHAMAR
# *
# def is_even(number, x=0, mmc=0):
#     if number % 2 == 0:
#         print('é par')
#     else:
#         print('é impar')
#     if number % mmc == 0:
#         print(f'{number} é divisivel por {mmc}')
#     else:
#         print(f'{number} não é divisivel por {mmc}')
# is_even(number, mmc=7)
# def _args(*args):
#     print(args)
# _args(1, 2, 3, 4, "aaaaa", True)
# def _kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print("{}, {}".format(k, v))
# _kwargs(a=1, b=2, c=3)
# def _args_kwargs(*args, **kwargs):
#     print(f"ARGS:\t{args}")
#     print(f"KWARGS:\t{kwargs}")
# _args_kwargs(1, 2, 3, 4, "aaaaa", True, a=1, b=2, c=3)
# def funcao_posicional(parametro_1, parametro_2, parametro_3, /):
#     print(f"parametro_1: {parametro_1}")
#     print(f"parametro_2: {parametro_2}")
#     print(f"parametro_3: {parametro_3}")
# funcao_posicional("Valor 1", "Valor 2", "Valor 3")
# def funcao_parametro_chave(
#     parametro_obrigatorio, *, parametro_1="", parametro_2="", parametro_3=""
# ):
#     print(f"parametro_obrigatorio: {parametro_obrigatorio}")
#     print(f"parametro_1: {parametro_1}")
#     print(f"parametro_2: {parametro_2}")
#     print(f"parametro_3: {parametro_3}")
# funcao_parametro_chave(
#     "valor obrigatorio",
#     parametro_1="Valor 1",
#     parametro_2="Valor 2",
#     parametro_3="Valor 3",
# )
# from timeit import timeit
# def func_test(a, b, c):
#     pass
# print(
#     f'Apenas Posicionais:\t\t{timeit("func_test(1, 2, 3)", number=1, globals={"func_test":func_test}):.8f} segundos'
# )
# print(
#     f'Apenas Parametros-Chave:\t{timeit("func_test(a=1, b=2, c=3)", number=1, globals={"func_test":func_test}):.8f} segundos'
# )
# def apresentar(nome="cool_name", idade=99, local="place"):
#     return f"Olá meu nome é {nome} e eu tenho {idade} anos e moro em {local}"
# def main():
#     """Função Principal"""
#     texto = apresentar("Mirai", local="casa")
#     print(texto)
# if __name__ == "__main__":
#     main()
# def mul(x, y):
#     return x * y

# print(f"função: {mul(3, 4)}")

# print(f"lambda: {(lambda a, b : a * b)(3, 4)}")

# p = print
# p("ola mundo")


# def capital(func, nome):
#     resposta = func(nome)
#     nome_maiusculo = resposta.upper()
#     return nome_maiusculo

# def apresentar(nome):
#     return f"olá {nome}"

# resultado_final = capital(apresentar,"Mirai")

# print(resultado_final)

# def apresentar(name):
#     return f"meu nome é {name}"


# def funcao_superior(func):
#     def funcao_interna(name):
#         resp = func(name)
#         return resp.upper()

#     return funcao_interna

#print(funcao_superior(apresentar)("Mirai"))



#~ FUNÇÂO              VALOR    OUT. FUNC      SOMA VAL + RES. FUNC
# func_alta_ord = lambda  x,        func:           x + func(x)
# print(func_alta_ord(2, lambda x: x**2))

# 1.  func_alta_ord = lambda x, func: x + func(x)
#     print(func_alta_ord(2, lambda y: y ** 2))

# 2.  func_alta_ord = lambda x, func: x + func(x)
#     func_alta_ord = lambda x,
#                     lambda y: y ** 2:
#                                     x + func(x)

# 3.  func_alta_ord = lambda x:
#                             x + lambda x: x ** 2

# 4.  print(func_alta_ord(2, lambda y: y ** 2))
#     func_alta_ord = lambda x:
#                             2 + lambda x: 2 ** 2


#! GLOBAL
# x = 3
# def local1():
#     y = 4
#     print(f"LOCAL1 (GLOBAL): {x}")
#     print(f"LOCAL1 (VAR L1): {y}")
#     print(f"LOCAL1 (VAR L2): {z}")
#     def local2():
#         global z = 23
#         # print(f"LOCAL2 (GLOBAL): {x}")
#         # print(f"LOCAL2 (VAR L1): {y}")
#         # print(f"LOCAL2 (VAR L2): {z}")


#     local2()

# local1()


# x = "Escopo Global"


# def func_legal_var_local():
#     x = "Escopo Local"
#     print(x)


# def func_legal_var_global():
#     global x
#     print(x)


# def alterar_global():
#     global x
#     x = "Alteramos a variavel global"


#print(x)  # Escopo Global
#func_legal_var_local()  # Escopo Local
#func_legal_var_global()  # Escopo Global
# alterar_global()
# print(x)  # Alteramos a variavel global

# numero_importante = 3

# def funcao1():
#     if numero_importante == 3:
#         print('aprovado')


# def funcao2():
#     global numero_importante
#     numero_importante = 4

# funcao2()
# funcao1()


# def func_extern1():
#     x = "Func externa 1"

#     def func_intern1():
#         x = "Func interna 1"
#         print(x)

#     print(x)
#     func_intern1()


# func_extern1()




# def func_extern2():
#     x = "Func externa 2"

#     def func_intern2():
#         nonlocal x
#         print(x)

#     print(x)
#     func_intern2()

# func_extern2()



# def func_extern3():
#     x = "Func externa 3"

#     def func_intern3():
#         nonlocal x
#         x = "Alteramos a variavel da Func Externa 3"
#         print(x)

#     print(x) # ANTES DE EDITAR
#     func_intern3() # EDITOU
#     print(x) # DPS

# func_extern3()


# x = 5 # GLOBAL

# def externa():
#     #x = 1

#     def interna():
#         x = 2
#         print("interna:", x)

#     def interna_nao_associada():
#         print("interna não associada:", x)

#     interna()
#     interna_nao_associada()
#     print("externa:", x)


# externa()
# print("global:", x)
# from numpy import array

# matriz_1 = [
#     [1, 2],
#     [3, 4]
# ]

# matriz_2 = [
#     [5, 6],
#     [7, 8]
# ]

# produto_das_matrizes = array(matriz_1) @ array(matriz_2)
# print(produto_das_matrizes)


# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# N, M, P = len(A), len(A[0]), len(B[0])

# result = []
# for i in range(N):
#     row = [0] * P
#     result.append(row)

# for i in range(N):
#     for j in range(P):
#         for k in range(M):
#             result[i][j] += A[i][k] * B[k][j]

# print(result)

# 2 + 3 #! OP BINARIO
# not True #! OP UNARIO

# x = 2

# resultado = "é maior q 4" if x > 4 else "é menor q 4"
# print(resultado)

# a = ["apple", "banana"]
# b = ["apple", "banana"]
# c = a

# print(f"A é igual a B ? {a == b}")
# print(f"A é B ? {a is b}")
# print(f"A é C ? {a is c}")

# print(f"A é diferente a B ? {a != b}")
# print(f"A não é B ? {a is not b}")
# print(f"A não é C ? {a is not c}")

# print(f"ID de B: {hex(id(b))}")
# print(f"ID de A: {hex(id(a))}")
# print(f"ID de C: {hex(id(c))}")

# print("h" in "abcdefghijklmnopqrstuvwxyz")
# print(12 not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

#print(bin(5))
# print(bin(8))

# a = 156
# b = 52
# print(f"A ({a}) = {bin(a)}")
# print(f"B ({b}) = {bin(b)}")
# print(f"A & B ({a & b}) = {bin(a & b)}")

# a = 156
# b = 52
# print(f"A ({a}) = {bin(a)}")
# print(f"B ({b}) = {bin(b)}")
# print(f"A | B ({a | b}) = {bin(a | b)}")

# a = 156
# b = 52
# print(f"A ({a}) = {bin(a)}")
# print(f"B ({b}) = {bin(b)}")
# print(f"A ^ B ({a ^ b}) = {bin(a ^ b)}")

# a = 156
# print(f"A ({a}) = {bin(a)}")
# print(f"Com Bit de Sinal: A ~ ({~a}) = {bin(~a)}")
# print(f"Sem Bit de Sinal: A ~ ({~a & 255}) = {bin(~a & 255)}")

# print(4 << 3)
# x = "Azul"                              #+ Associação
# x == "Carro"                            #+ Comparação

# if x == "Carro":                        #! Obrigatorio ter 1 if no inicio
#     print("Carro é igual a Carro")
# elif x == "Pessoa":                     #? Quantos Quiser
#     print("Pessoa é igual a Pessoa")
# elif x == "Azul":                       #? Quantos Quiser
#     print("Azul é igual a Azul")
# else:                                   #! Obrigatorio ter 1 else no fim
#     print("x não é igual a nada")

# #*  Para ter cadeias de elif você deve ter 1 if no inicio
# #*  e um else no final, porém não é obrigatorio para if-else e if
# #*  ou seja, se tivermos apenas um if, não precisamos de um else
# #*  e se tivermos um if e um else, não precisamos de um elif


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


# # resposta = ''
# # while resposta != "sair":
# #     resposta = input('insira a resposta: ')

# # x = 0           #~ declarando x
# # while x < 10:   #~ enquanto x for menor que 10
# #     print(x)    #~ exibir x
# #     x += 1      #~ aumentar x por 1


# for i in range(10):
#     print(i)

# def exibir_lista_comidas():
#     comidas = ['arroz', 'pão', 'feijão']

#     if type(comidas) == type([]):
#         print(comidas)
#     else:
#         print('del sys')

# exibir_lista_comidas()

# dicionario_aleatorio = {
#     "Chave A": "Valor 01",
#     "Chave B": "Valor 02",
#     "Chave C": "Valor 03",
# }

# for chave, valor in dicionario_aleatorio.items():
#     print(chave, valor)

# for i in range(1, 21):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# A = [1, 5, 4, 2, 3, 7, 0, 8, 6, 9]
# print(A[4:7])


# lista_normal = [1, 2, 3, 4, 5]
# lista_dobrada = [i * 2 for i in lista_normal]
# print(f"lista_normal: {lista_normal}")
# print(f"lista_dobrada: {lista_dobrada}")


# lista_normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_de_pares = [i for i in lista_normal if i % 2 == 0]
# print(f"lista_normal: {lista_normal}")
# print(f"lista_de_pares: {lista_de_pares}")
#   Dicionário -> Estudante
#   Nome, Idade, Notas -> lista
#
#   calcule a média das notas
#   se for superior ou igual a 6
#       exiba "Aprovado"
#   se não exiba "Reprovado"


# estudante = {
#     "nome": "roberbo",
#     "idade": 15,
#     "notas": [6, 6, 6, 6, 6, 6],
# }

# media = sum(estudante["notas"]) / len(estudante["notas"])
# print(f"seu nome é {estudante['nome']} sua idade é {estudante['idade']} e você foi")

# if media >= 6:
#     print("aprovado")
# else:
#     print("reprovado")



#   Menu
#       (1) - exibir "opcao 1"
#       (2) - exibir "opcao 2"
#       (0) - Sair
#
#   Enquanto o Usuário não digitar 0
#   exibir o menu, e caso ele digite
#   alguma das opções exiba a opção
#
#   caso ele digite algo que não é uma opção
#   exiba "Opção não encontrada", e exiba o menu

# for i in [1, 3, 4, 7, 9]:
#     if i % 2 == 0:
#         print("contem um numero par")
#         break
# else:
#     print("não contem um numero par")


# # r idx: -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
# # index:   0   1   2   3   4   5   6   7   8   9
# A   =     [1,  5,  4,  2,  3,  7,  0,  8,  6,  9]

# print(A[-8:])


# lista_de_pares = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         lista_de_pares.append(i)

# def checar_amigo(lista_amigos_argumento, lista_pessoas_argumento):
#     for pessoa in lista_pessoas_argumento:
#         if pessoa in lista_amigos_argumento:
#             print(f'olá amigo')
#         else:
#             print(pessoa)


# lista_pessoas = [
#     'pessoa00',
#     'pessoa01',
#     'pessoa02',
#     'pessoa03',
#     'pessoa04',
#     'pessoa05',
#     'pessoa06',
#     'pessoa07',
#     'pessoa08',
#     'pessoa09',
#     'pessoa10',
#     'pessoa11',
#     'pessoa12',
#     'pessoa13',
#     'pessoa14',
#     'pessoa15',
#     'pessoa16',
#     'pessoa17',
#     'pessoa18',
#     'pessoa19',
# ]

# lista_amigos = ['pessoa01', 'pessoa02', 'pessoa09', 'pessoa13']
# lista_pessoas2 = [
#     'pessoa00',
#     'pessoa01',
#     'pessoa02',
#     'pessoa03',
#     'pessoa04',
#     'pessoa05',
#     'pessoa06',
#     'pessoa07',
#     'pessoa08',
#     'pessoa09',
#     'pessoa10',
#     'pessoa11',
#     'pessoa12',
#     'pessoa13',
#     'pessoa14',
#     'pessoa15',
#     'pessoa16',
#     'pessoa17',
#     'pessoa18',
#     'pessoa19',
# ]


# checar_amigo(lista_amigos, lista_pessoas)
# print("==========================")
# checar_amigo(lista_amigos, lista_pessoas2)


#   Uma função, que tem um nome como parametro
#   ela tem que exibir/printar uma apresentação
#
#   Olá meu nome é...



# def apresentar(nome="nome_legal", idade=99): # Parametro
#     if nome == "":
#         nome = "nome_legal"
#     if idade == "":
#         idade=99


#     print(f"Olá {nome} e eu tenho {idade} anos")


# resposta = input("Insira seu nome e sua idade (separados por ,): ")

# resposta_junta = resposta.replace(" ", "")
# if resposta_junta != "":
#     resposta_separada = resposta_junta.split(',')
# else:
#     resposta_separada = ["",""]

# apresentar(
#     nome=resposta_separada[0],
#     idade=resposta_separada[1]
# ) # Argumento

# endregion


carro = "Ford"

if carro == "Wolkswagen" :
    ...
elif carro == "BMW":
    ...
elif carro == "Pegeout":
    ...
elif carro == "Ferrari":
    ...
else:
    ...

match carro:
    case "Wolkswagen":
        ...
    case "BMW":
        ...
    case "Pegeout":
        ...
    case "Ferrari":
        ...
    case _:
        ...
