#class A:

   # a = 2

  #  def teste():
 #       pass



#class B:

    #a = 6

 #   def maisum():
  #        pass

 # não funciona



#print(f"While Loop:\t{timeit(pure_while, number=1)} segundos")
#print(f"For Loop:\t{timeit(pure_for, number=1)} segundos")
from random import randint


print ('começando jogo')


random = randint(0, 24)

tentativas = 0;

chances = 10;

while tentativas != random:
    tentativas = input('tenta pensar de maluco um número de 0 a 24:')
    if tentativas.isnumeric():
        tentativas = int(tentativas)
    chances = chances - 1
    if tentativas == random:
        print('')
        print('Parabéns< você conseguiu estranho! O número era {} e você ainda tinha {} chances.'.format(random, chances))  
        print('')
        break;
    else:
        print('')
        if tentativas > random:
            print('Você errou idiota!!! Dica: É um número menor.')
        else:
            print('Você errou seu idiota!!! Dica: É um número maior.')
        print('você ainda tem {} chances.'.format(chances))
        print('')
    if tentativas == 0:
        print ('')
        print('Suas tentativas acabaram, você perdeu vacilão!')
        print('')
        break;



print( ' o jogo acabou pode kitar bobão')

       