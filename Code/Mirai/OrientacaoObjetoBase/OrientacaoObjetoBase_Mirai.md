<!-- Markdown -->
<!--#region OLD_CODE -->
Pessoas:
    Propriedades:
        - Nome
        - Idade
        - Residencia
    Metodos:
        - Andar
        - Falar
        - Correr
<!--#endregion -->

Atributo => Guarda Valor -> Variaveis
Metodo   => Ação -> que PODE usar atributos.

nós temos um estudante com um nome, uma profissão (estudante) e que contem 5 notas e queremos calcular a média delas.

nós poderiamos representar este estudante como um dicionário, e usar sum() / len().


class NOME:
    def __init__(self):
        {codigo}



class -> é a keword de declaração de uma classe
{Nome} -> o nome da classe
def __init__(self): -> um método especial, essencialmente, é executado toda vez que a classe é instanciada, é usado para guardar as propriedades dessa instancia.
self -> um parametro especial, se refere a classe em si
{codigo} -> o codigo para ser executado



*Classe* x *Objetos* x *Instancias*

*Um Objeto é uma Instancia de uma Classe.*



classe professor:
    - Atributo de Classe
    - 3 Atributos de instancia
    - Metodo -> apresentar
