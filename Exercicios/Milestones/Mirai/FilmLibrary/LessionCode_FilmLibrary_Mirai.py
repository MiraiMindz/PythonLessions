'''Biblioteca de Filmes - Milestone 01
Esse programa foi escrito como primeiro desafio no curso de Python

Um programa que coleta, armazena e mostra os filmes do usuário.

Tarefas:
    [x] - Menu
    [x] - Ajuda
    [x] - Adicionar Filmes
    [x] - Pesquisar Filmes
    [x] - Mostrar Filmes

Observações:
    Um menu usando while loop
    As opções devem ser divididas em funções

AUTOR: Mirai
DATA: 24/10/22 - 24/10/22'''


MENU = """Escolha uma opção:
(1) - Adicionar um Filme
(2) - Pesquisar um Filme
(3) - Ver Todos os Filmes
(4) - Ajuda
(0) - Sair"""

HELP_MESSAGE = """Ultilize os numeros para navegar e pressione ENTER para enviar sua resposta.
Uma Explicação de cada opção:
\t"(1) - Adicionar um Filmes"
\t\t- Esta opção é a principal do programa, você adicionará as seguintes informações do filme:
\t\t\t- Titulo
\t\t\t- Ano
\t\t\t- Sinopse
\t"(2) - Pesquisar um Filme"
\t\t- Nesta opção você será perguntado por um termo
\t\t  caso ele não se encontre no banco de dados, você retornará ao menu principal
\t"(3) - Ver Todos os Filmes"
\t\t- Exibe todos os filmes no banco de dados
\t"(4) - Ajuda"
\t\t- Exibe este menu de ajuda
\t"(0) - Sair"
\t\t- Sai do programa"""


lista_filmes = []


def clear_console():
    """Função que limpa o console"""
    print("\033c", end='')


def show_help():
    """Exibe a ajuda"""
    print(HELP_MESSAGE)


def print_menu():
    """Exibe o menu"""
    print(MENU)


def add_film():
    """Adiciona Filmes"""
    _dicionario_filme = {}
    _dicionario_filme["nome"] = input("Insira o nome do filme: ")
    _dicionario_filme["ano"] = input("Insira o ano do filme: ")
    _dicionario_filme["sinopse"] = input("Insira o sinopse do filme: ")
    lista_filmes.append(_dicionario_filme)


def search_film():
    result = ""
    term = input("Insira o nome do filme: ")
    for _x in lista_filmes:
        if _x["nome"].lower() == term.lower():
            result = _x
            break
        result = ""


    if result:
        print(f"\tNome: {result['nome'].capitalize()}")
        print(f"\tAno: {result['ano']}")
        print(f"\tSinopse: {result['sinopse'].capitalize()}")
    else:
        print("Filme não encontrado")


def show_films():
    for i, v in enumerate(lista_filmes):
        print(f"Filme {i:0>2}")
        print(f"\tNome: {v['nome']}")
        print(f"\tAno: {v['ano']}")
        print(f"\tSinopse: {v['sinopse']}")


def menu(resposta):
    """O menu da aplicação"""
    if resposta == 1:
        clear_console()
        add_film()
    elif resposta == 2:
        clear_console()
        search_film()
    elif resposta == 3:
        clear_console()
        show_films()
    elif resposta == 4:
        clear_console()
        show_help()
    elif resposta == 0:
        clear_console()
    else:
        clear_console()
        print("Opção não reconhecida, favor tentar novamente")


def main():
    """Função Principal"""
    clear_console()
    print("Bem vindo a Biblioteca de Filmes")

    print_menu()
    resposta = int(input("> "))
    menu(resposta)

    while resposta:
        print_menu()
        resposta = int(input("> "))
        menu(resposta)


if __name__ == '__main__':
    main()
