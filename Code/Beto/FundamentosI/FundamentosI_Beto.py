#region_________________ 

    # nome_variavel = 34
    # camel_Case = 'yee'
    # CapitalCase = 3
    # snake_case = True

# # - print('Olá Mundo')

    # resposta = input('qual e a sua idade? ')
# input('sua idade e 14?')
    # tem = input('voce tem certeza? ')

  #imprimir = print
  #imprimir('Ola Mundo')
#endregion

#region ______________


# string_1 = 'essa string usa aspas simples'
# string_2 = "essa string usa aspas duplas"

# print(string_1,  type(string_1))
# print(string_2,  type(string_2))

# print(string_1)
# print(string_2)

# apresentaçao = "Hi, my name is Betoo, I'm a Developer"
# print(apresentaçao)
# citacao = 'pois então ela disse, "não se dirija mais a mim"...'
# print(citacao)

# citacao = "Pois então ela disse, \"Não se dirija mais a mim\"..."
# print(citacao)

#endregion

# multi_fstring = f'''

# '''

# x = 0
# x += 1

# exemplo_1 = 8 / 4
# exemplo_2 = 1 / 3
# exemplo_3 = 8 // 4
# exemplo_4 = 1 // 3

# print(f'8 /  4:\t{exemplo_1}\t{type(exemplo_1)}\t\t(Divisão)')
# print(f'1 /  3:\t{exemplo_2:.2f}\t{type(exemplo_2)}\t\t(Divisão)')
# print(f'8 // 2:\t{exemplo_3}\t{type(exemplo_3)}\t\t(Divisão Verdadeira)')
# print(f'1 // 3:\t{exemplo_4}\t{type(exemplo_4)}\t\t(Divisão Verdadeira)')

# print(True  and  True)
# print(True  and  False)
# print(False and  True)
# print(False and  False)
# print(True  or True)
# print(True  or False)
# print(False or True)
# print(False or False)
# print(not False)
# print(not True)


tulipa_numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(tulipa_numeros, type(tulipa_numeros))

x, y = 1, 2
z = x, y
print("TUPLE:", z, "ENDEREÇO MEM:", hex(id(z)))
z = x, y, 3
print("TUPLE:", z, "ENDEREÇO MEM:", hex(id(z)))

lista = [1, 2, 3]
print("LISTA:", lista, "ENDEREÇO MEM:\t\t", hex(id(lista)))
lista.append(4)
print("LISTA:", lista, "ENDEREÇO MEM:\t", hex(id(lista)))

#[ INDEX:               0         1          2          3
#? REVERSE-INDEX:      -4        -3         -2         -1
lista_amigos = ['Mirai', 'Beto',    'Kaal',   'Joaquim']
print(lista_amigos[-3])


#? ADICIONAR:
#* [x] list.append()
#* [x] list.insert()
#? REMOVER:
#! [x] list.pop()
#! [x] list.remove()

lista_amigos = ['Mirai', 'Beto', 'Kaal', 'Joaquim']
print(lista_amigos)

lista_amigos.remove('Kaal')

print(lista_amigos)

matriz = [
#*X  0  1  2     Y
    [1, 2, 3],#* 0
    [4, 5, 6],#* 1
    [7, 8, 9] #* 2
]
#*           Y  X
print(matriz[0][2])

Alunos_de_Ciencias   = {'Mirai', 'Mine', 'Ramon'}

print(f'Antes de adicionar o Beto:\t{Alunos_de_Ciencias}')
Alunos_de_Ciencias.add('Beto')
print(f'Depois de adicionar o Beto:\t{Alunos_de_Ciencias}')

print(f'Antes de remover o Mine:\t{Alunos_de_Ciencias}')
Alunos_de_Ciencias.remove('Mine')
print(f'Antes de remover o Mine:\t{Alunos_de_Ciencias}')


Alunos_de_Matematica = {'Mirai', 'Luis', 'Ramon'}
Alunos_de_Portugues  = {'Kaal', 'Ramon', 'Mine'}
Alunos_de_Ciencias   = {'Mirai', 'Mine', 'Ramon'}

sets_difference = Alunos_de_Matematica.difference(Alunos_de_Portugues)
sets_symmetric_difference = Alunos_de_Matematica.symmetric_difference(Alunos_de_Portugues)
sets_intersection = Alunos_de_Matematica.intersection(Alunos_de_Portugues)
sets_union = Alunos_de_Matematica.union(Alunos_de_Portugues)
print(f'Diferença entre Alunos de Matematica e Português:\n\t{sets_difference}')
print(f'Diferença simétrica entre Alunos de Matematica e Português:\n\t{sets_symmetric_difference}')
print(f'Interseção entre Alunos de Matematica e Português:\n\t{sets_intersection}')
print(f'União entre Alunos de Matematica e Português:\n\t{sets_union}')

valor1, valor2, chave1, chave2 = "valor1", "valor2", "chave1", "chave2"


dicionario = {
    chave1: valor1,
    chave2: valor2,
}

dicionario['chave3'] = 'valor3'
dicionario['chave2'] = 'carro'
dicionario.pop('chave2')
print(dicionario)

x = 3
print(x, type(x))
y = str(x) # converte 3 int em "3" string
print(y, type(y))

notas = [9.4, 9.0]

soma = sum(notas)

comprimento = len(notas)

media = soma / comprimento

print(media)

x = oct(18)

print(x)