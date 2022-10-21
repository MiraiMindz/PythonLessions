''' Biblioteca de Filmes

TODO:
    [x] - Criar os filmes
    [/] - Menu
    [x] - Implementar as condicionais

AUTOR: Karllos
DATA: 24/9/2022 - ???'''

movieName = ['Batman', 'Sherlock Holmes', 'Star Wars']
movieYear = [2022, 1993, 1978]
movieSinopse = ['cavaleiro das trevas', 'detetive', 'guerras galacticas']

print('Bem vindo a Biblioteca de Filmes do Karllos\nEscolha uma opção:\n(1) - Adicionar um Filme\n(2) - Pesquisar um Filme\n(3) - Ver todos os Filmes\n(4) - Ajuda\n(0) - Sair\ninsira algo:')
choicedMovie = int(input())
print("\033c", end='')

while choicedMovie:
    def option1(newMovie, newMovieYear, newMovieSinopse):
        '''a partir dos parametros adiciona itens na lista dos filmes'''
        movieName.append(newMovie), movieYear.append(newMovieYear), movieSinopse.append(newMovieSinopse)     
        quit()
    def option2(search):
        '''pesquisa o filme na biblioteca'''
        print(f'Nome: {movieName[search]}\nAno: {movieYear[search]}\nSinopse: {movieSinopse[search]}')
        quit()
    def option3():
        '''mostra todos os itens na biblioteca'''
        print(f'Filmes Nome: {movieName}\nFilmes Ano: {movieYear}\nFilmes Sinopse: {movieSinopse}')
        quit()
    def option4():
        '''menu de ajuda da biblioteca'''
        print('Utilize os números para navegar e pressione ENTER para enviar a sua resposta.\nopção (1) é a principal do programa você pode adicionar um título um ano e uma sinopse e ele será direcionado a biblioteca de filmes automaticamente.\nopção (2) você pesquisa um filme no banco de filmes, se ele estiver na biblioteca então será retornado.\nopção (3) você visualiza todos os filmes da biblioteca.\nopção (4) exibe este menu de ajuda.\nopção (5) você sai do programa.')
        quit()

    option1(input('diga o nome do novo filme: '), input('diga o ano desse filme: '), input('diga a sinopse: ')) if choicedMovie == 1 else ""
    option2(int(input('insira o numero do filme na lista: '))) if choicedMovie == 2 else ""
    option3() if choicedMovie == 3 else ""
    option4() if choicedMovie == 4 else ""
