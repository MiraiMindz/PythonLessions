


# informacoes = {
# "nome": "roberbo",
# "idade":(15),
# "notas":(1, 2, 3, 4, 5, 6),
# }
# media = sum(informacoes["notas"]) / len(informacoes["notas"])

# print(f"seu nome é {informacoes['nome']} sua idade é {informacoes['idade']} e você foi")

# if media > 6:
#    print("aprovado")

# if media < 6:
#    print("reprovado")



# menu = """
# start (1)
# opções (2)
# sair (3)

# obs(aperte espaço uma vez antes de digitar)
# """

# R = input("->")

# while R != "3" :
#    print (f"""# {menu}
#    {R}
#    """)
#    R = input("->")
#    if R == "1":
#        print("""
#        !!!você selecionou start!!!""")

#    elif R == "2":
#        print("""
#        !!!você selecionou opções!!!""")

#    elif R == "3":
#        print("""
#        !!!você saiu!!!""")

#    else:
#        print("""
#        !!! Opção não encontrada !!!""")

# corrigido

# menu = '''================================================
# \t(1) - opcao_1
# \t(2) - opcao_2
# \t(3) - opcao_3
# \t(0) - sair
# ================================================'''

# resposta = 1
# while resposta:
#    print(menu)
#    resposta = int(input("Insira sua Resposta: "))
#    if resposta == 1:
#        print('opcao 1')
#    elif resposta == 2:
#        print('opcao 2')
#    elif resposta == 3:
#        print('opcao 3')
#    elif resposta == 0:
#        break
#    else:
#        print('resposta não encontrada')

# for num in range(1, 21):

#     if num % 3 == 0 and num % 5 == 0 :
#         print("fizz buzz")

#     elif num % 3 == 0:
#         print("fizz")

#     elif num % 5 == 0:
#         print("buzz")

#     else:
#         print(num)

# for num in ["numero1", "numero2", "numero3"]:
#     print(f"o primeiro numero é {num}, o segundo é {num}, o terceiro é {num} ")

def nomes2(nomes):
    print(f"Olá, eu sou {nomes}")

nomes2("roberbo")