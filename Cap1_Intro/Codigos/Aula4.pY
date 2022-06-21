#!/usr/bin/env python3.10

# region

# if (x == 1):
#     print("algo")
# elif (x == 2):
#     print("algo")
# else:
#     print("algo")

# UM IGUAL (=) ALGO É IGUAL A OUTRA COISA
# DOIS IGUAIS (==) ISSO É IGUAL AQUILO?
# EXCLAMAÇÃO (!) INVERTE, ISSO NÃO É IGUAL AQUILO?

# for i in range(10):
#     print(i)

#   Um programa pra achar numeros primos usando um for loop
#       - for

# ========================================================

# numero = int(input("Insira um numero: "))
# def primo(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True

#     for i in range(2, numero):
#         if numero % i == 0:
#             return False

#         return True

# x = primo(numero)
# if x:
#     print("é primo")
# else:
#     print("não é primo")

# ========================================================

# numero = int(input("Insira um numero: "))
# def primo(n):
#     '''É função para achar numeros primos'''
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True

#     for i in range(2, numero):
#         if numero % i == 0:
#             return False

#         return True

# x = primo(n=numero)
# if x:
#     print("é primo")
# else:
#     print("não é primo")


# endregion

# def soma(*args, **kwargs): # DEFINIR
#     '''Retorna a soma entre dois valores'''
#     resultado = 0
#     for i in kwargs.values():
#         resultado += i
#     summ = sum(args)

#     print(kwargs)
#     return resultado, summ



# print(soma(a=3,b=2,c=3,d=4,e=56,f=7,g=8,h=9,i=0,j=314,k=454))


# def func(a=2):
#     print(a)

# func(7)

# VARIAVEL = lambda {variaveis_lambda} : {função}

# soma = lambda x, y, z : x + y + z

# print(soma(1, 2, 3))


# def summ(): #  Alta Ordem
#     def()
#     return lambda _ : print("aaaa")

# summ()


# def a():
#     v = 2
#     def b():
#         vx = 3
#         print(vx)
#     b()
#     print(v)

# # v = 2
# # print(v)


# a()


# a, b = 2, 3

# # {SE VERDADE} if {EXPRESSAO} else {SE FALSO}

# x = ["a", "b", "c", "d"]
# print("a" in x)

