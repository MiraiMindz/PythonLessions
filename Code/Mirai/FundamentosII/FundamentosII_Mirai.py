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
# endregion
# endregion
