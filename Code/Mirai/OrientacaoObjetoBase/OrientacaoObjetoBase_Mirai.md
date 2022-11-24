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

pessoa:
    - Atributos:
      - nome
      - idade
      - residencia

    - metodos:
      - andar
      - correr
      - falar

nós temos um estudante com um nome, uma profissão (estudante) e que contem 5 notas e queremos calcular a média delas.

class {Nome}:
    def __init__(self):
        {codigo}


Classe, Objetos e Instancias

Metodos Mágicos (Magic Methods/Dunder Methods)

__init__(x) -> Executado assim que um novo objeto é instanciado.
__call__(x) -> Executado quando uma instancia é chamada como função.
__name__(x) -> Retorna o nome da classe cujo o objeto foi instanciado.
__repr__(x) -> Retorna uma string de representação da classe.

__new__() -> Executado para criar uma nova instancia de uma classe.

class {nome}({classe pai}):
    def __init__(self, {variaveis da classe pai}):
        super().__init__({variaveis da classe pai})


<!--#endregion -->

criem uma lista de quadrados, baseada em uma outra lista

[1, 2, 3] -> [1, 4, 9]


