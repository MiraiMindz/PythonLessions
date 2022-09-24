Controle de Fluxo (Control Flow) Escopo

- Sequencial
- Decisivo (Se e Se não)
- Repetitivo
- Funcional

se for é se não for não

se {nick do cara} estiver em {os_malucolá} exibir "Olá amigo", caso contrário, exibir "Olá estranho"

'if' e o 'else'
if {condição}:
    {codigo} # SE FOR SIM
else:
    {código} # SE FOR NÃO

ESCOPO
O Escopo é sempre de fora para dentro, nunca de dentro para fora.
1. Global
2. A
3. B
4. C   

GLOBAL
    GLOBAL {
x = 3
    A {
        print(x)
        B {
            print(x)
            C {
                print(x)
            }
        }
    }
}

GLOBAL
x = 3
    A
        print(x)
        B
            print(x)
            C
                print(x)

match {variavel}:
    case {possivel valor}:
        {codigo}
    case {possivel valor}:
        {codigo}
    case {possivel valor}:
        {codigo}
    case _:
        {codigo}


While --> ENQUANTO for verdade executar isso.Ou quando o x for menor que 10,execute o códigoi abaixo:
    print(f"valor de x: {x}") -->

for --> PARA

for {index} in {raio}:
    {código}