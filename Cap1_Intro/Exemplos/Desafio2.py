#!/usr/bin/env python3.10


# DESAFIO:
#   Escrever um programa que pega uma lista de numeros, e retorna a media deles


# #region Desafio Original:
# raw_list = input("Insira a lista: ")
# lista_end = list(raw_list.replace(" ", "").split(','))
# int_list = list(map(int, lista_end))
# media = sum(int_list) / len(int_list)
# print(f"Media: {media}")
# #endregion

# #region Desafio Dicionario:
# print("Insira uma com a seguinte formatação:\n\tMATERIA:NOTA,MATERIA:NOTA")
# raw_list = input("Insira a lista: ")
# lst_end = list(raw_list.replace(" ", "").split(","))

# materias = [i.split(':')[0] for i in lst_end]
# notas = [i.split(':')[1] for i in lst_end]

# int_notas = list(map(int, notas))
# media_notas = sum(int_notas) / len(int_notas)
# notas_dict = dict(zip(materias, int_notas))
# notas_dict["media"] = media_notas
# print(notas_dict)
# #endregion
