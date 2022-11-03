#!/usr/bin/env python3.10
# pylint: disable=all
# Python
#region OLD_CODE
#endregion

# estudante = {
#     "Nome": "Joaquim",
#     "Notas": [8.6, 9.3, 7.5, 8.8, 7],
#     "Profissao": "Estudante",
# }

# media = sum(estudante["Notas"]) / len(estudante["Notas"])

# print(f"O {estudante['Profissao']} {estudante['Nome']} tem média {media:.2f}")

# class Estudante:
#     profissao = "Estudante"  # esse é um Atributo de classe
#     def __init__(self, nome, notas):
#         self.notas = notas  # esse é um Atributo de Instancia
#         self.nome = nome  # esse é um Atributo de Instancia

#     def calc_med(self):  # esse é um metodo
#         self.media = sum(self.notas) / len(self.notas)



# estudante_joaquim = Estudante("Joaquim", [5.5, 3.8, 7.3, 4.5, 2.5])
# #~ estudante_joaquim é um objeto instanciado da classe Estudante

# estudante_joaquim.calc_med()
# print(
#     f"O {estudante_joaquim.profissao} {estudante_joaquim.nome} tem a media {estudante_joaquim.media}"
# )


class Estudante:
    def __init__(self, nome, notas):
        self.notas = notas
        self.nome = nome

    def calc_med(self):
        self.media = sum(self.notas) / len(self.notas)


estudante_mirai = Estudante("Mirai", [8.6, 9.3, 7.5, 8.8, 7]) #! CONSTRUTOR
#~ estudante_mirai é um objeto instanciado da classe Estudante
