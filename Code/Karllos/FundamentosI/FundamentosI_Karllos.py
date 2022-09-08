# print('hello world')

# entrada = input
# digite = print

# day = entrada('Anata ga umaretahi o oshietekudasai:')
# mouth = entrada('umareta tsuki o oshietekudasai:')
# year = entrada('umareta toshi o oshietekudasai:')

# birthday = (day + '/' + mouth + '/' + year)

# digite('Anata wa sonohi ni uma reta', birthday)

# print(f"um texto muito bonito!\nolha só quebrei a linha em um print 'o'")

# num1 = int(input('type a number:'))
# num2 = int(input('type another number:'))

# s = num1 + num2

# print(s)

# lista = [1, 'Pastel', True]
# print(lista)

#! Index
#**           0        1       2        3        4
#FundamentosI_Karllos
#* Reverse Index
#?           -5       -4      -3       -2       -1
#friends = ['Mirai', 'Mine', 'Ramon', 'Kaal', 'Kanddrex']

# print(friends)
# print(friends[0])
# print(friends[-5])

# friends.append('Beto')

# print(friends)

# friends.insert(0, 'Pão de batata')

# print(friends)

# friends.pop(1)
# friends.remove('Kanddrex')

# print(friends)

# matriz = [
# #X          0                   1                   2            Y
#     ['farinha de trigo', 'farinha de leite', 'farinha de mesa'],  #0
#     ['carne grelhada', 'carne bem passada', 'carne mau passada'], #1
#     ['bolo', 'pudim', 'sorvete']                                  #2
# ]

# print(matriz[1][1])

# conjunto = {'Kaal', 'Mirai', 'Ramon'}

# print(conjunto)

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

# notas = [6, 7, 5]
# soma = sum(notas)
# comprimento = len(notas)
# media = (soma / comprimento)

# print(f'o tipo da lista é claramente: {type(notas)}.')
# print(f'a soma da lista é {soma}.')
# print(f'o comprimento da lista é {comprimento}.')
# print(f'a media é {media}.')

# if(media >= 6):
#     print('parabéns o aluno passou!')
# else:
#     print('reprovou fião, sinto muito')

# from math import trunc

# num = float(input('type a number:'))
#* with import 
# print(f'the int part of {num} is {trunc(num)}')

# num = float(input('type a number:'))
#? not import (better)
# print(f'the int part of {num} is {int(num)}')

# from math import sqrt

# co = float(input('digite um valor pro cateto:'))
# ca = float(input('agora um pro adjacente:'))
# h = sqrt((co ** 2) + (ca ** 2))

# print(f'a hipotenusa vai medir {hipotenusa:.2f}')

# from random import choice, shuffle

# stds = ['Kaal', 'Mine', 'Kanddrex', 'Betoo', 'Rick Astley bombado', 'Ramon']

# print(f'the chosen student was {choice(stds)}')

# shuffle(stds)

# print(f'the order of presentation chosen was {stds}')


# import pygame

# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load('sounds/lofi.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

# from playsound import playsound

# playsound('/sounds/lofi.mp3/')

# name = input('type your name:')

# friends = ['Mirai', 'Kaal', 'Kanddrex', 'Betoo', 'Joseph']
# Mine =    ['Mine']

# if(name in friends):
#     print('Welcome back!')
# elif(name in Mine):
#     print('Hello Minecraft')
# else:
#     print("Hello stranger '-'")    

# number = int(input("type a number to find out if it is even or odd:"))

# if( number % 2 == 0):
#     print('even')
# else:
#     print('odd')

# x = 0

# while x < 10:
#   print(f"valor de x: {x}")
#   x += 1

# for i in range(11):
#     print(i)
#     i += 1

# for num in range(100):
#     if num % 15 == 0:
#         print("'FizzBuzz'")
#     elif num % 3 == 0:
#         print("'Fizz'")
#     elif num % 5 == 0:
#         print("'Buzz'")
#     else:
#         print(num)

# num = [1, 3, 2]
# num.sort()

# print(num)

list_results = []
