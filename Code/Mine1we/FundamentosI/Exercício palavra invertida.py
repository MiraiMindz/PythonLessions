import re

m = re.findall(r"[^\-,.?!\s]+", "mentiras disseram verdades!")[::-1]
#** findall() retorna uma lista contendo todas as correspondências não sobrepostas de um padrão dentro de uma string.
#*  [^\-,.?!\s]+ Apanha um ou mais caracteres que não sejam ou - ou , ou . ou ? ou ! ou um de espaço.
#!  [::-1] pega a lista obtida com findall() e a retorna invertida.
print(*m)
