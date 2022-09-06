

#from decimal import localcontext


# prompt = "insira algo -> "


# texto = input(prompt)

#aaaaaa

# print('''

# aaaaaa 

# ''')

# cparentesamigo = (

#            "ta voando",                                   

 #                "faz certo",                
  #                                      "loco", 

   #                         "é"
#)

#print(cparentesamigo)

from timeit import timeit

def pure_while(n: int = 100000000) -> int:
    i, x = 0, 0
    while i < n:
        x += i
        i += 1
    return x

def pure_for(n: int = 100000000) -> int:
    x = 0
    for i in range(n):
        x += i
    return x



print(f"While Loop:\t{timeit(pure_while, number=1)} segundos")
print(f"For Loop:\t{timeit(pure_for, number=1)} segundos")