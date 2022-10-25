''' Biblioteca de Filmes

TODO:
    [x] - Criar os filmes
    [x] - Menu
    [x] - Implementar as condicionais

AUTOR: Karllos
DATA: 24/9/2022 - 24/10/2022'''

movieName = ['batman', 'sherlock holmes', 'star wars']
movieYear = [2022, 1993, 1978]
movieSinopse = ['cavaleiro das trevas', 'detetive', 'guerras galacticas']

def clearConsole():
    print("\033c", end='')

def showMenu():
    print('Bem vindo a Biblioteca de Filmes do Karllos\nEscolha uma opção:\n(1) - Adicionar um Filme\n(2) - Pesquisar um Filme\n(3) - Ver todos os Filmes\n(4) - Ajuda\n(0) - Sair')

print("\033c", end='')

def addMovie(newMovie, newMovieYear, newMovieSinopse):
    '''a partir dos parametros adiciona itens na lista dos filmes'''
    movieName.append(newMovie), movieYear.append(newMovieYear), movieSinopse.append(newMovieSinopse)     
def searchMovie(search):
    '''pesquisa o filme na biblioteca'''
    pos = movieName.index(search.lower())
    print(movieName[pos]), print(movieYear[pos]), print(movieSinopse[pos])
def showMovies():
    '''mostra todos os itens na biblioteca'''
    print(f'Filmes Nome: {movieName}\nFilme Ano: {movieYear}\nFilme Sinopse: {movieSinopse}')
def helpMessage():
    '''menu de ajuda da biblioteca'''
    print('Utilize os números para navegar e pressione ENTER para enviar a sua resposta.\nopção (1) é a principal do programa você pode adicionar um título um ano e uma sinopse e ele será direcionado a biblioteca de filmes automaticamente.\nopção (2) você pesquisa um filme no banco de filmes, se ele estiver na biblioteca então será retornado.\nopção (3) você visualiza todos os filmes da biblioteca.\nopção (4) exibe este menu de ajuda.\nopção (5) você sai do programa.')

def menuLogic(choice):
    if choice == 1:
        clearConsole()
        addMovie(input("diga o nome do novo filme: "), input("diga o ano desse filme: "), input("diga a sinopse: "))
        print("pedido de novo filme realizado com sucesso!")
        print("\n")
    elif choice == 2:
        clearConsole()
        searchMovie(input("insira o nome do filme: "))
        print("\n")
    elif choice == 3:
        clearConsole()
        showMovies()
        print("\n")
    elif choice == 4:
        clearConsole()
        helpMessage()
        print("\n")
    elif choice == 0:
        clearConsole()
    else:
        clearConsole()
        print("escolha não existente.")
        print("\n")

showMenu()
choicedMovie = int(input("> "))
menuLogic(choicedMovie)

while choicedMovie:
    showMenu()  
    choicedMovie = int(input("> "))
    menuLogic(choicedMovie)