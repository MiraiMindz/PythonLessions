"""Script feito para padronizar e automatizar a criação de arquivos pertinentes as milestones"""
import sys
from getopt import getopt
from ntpath import basename
from ntpath import split
from os import getcwd
from os import makedirs
from os import path
from pathlib import Path
from platform import system
from sys import argv

HELP_MESSAGE = """Uso:
\tpython3 generate_milestones.py [-h] [-n] [-c] name milestone_num

Um script feito para automatizar/padronizar a criação de arquivos pertinentes as milestones.

Options:
\t-h, --help\t\tExibe esta ajuda
\t-n, --name\t\tEspecifica o nome
\t-c, --milestone_num\tEspecifica o numero da milestone

As opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero da milestone seguindo a ordem
Caso nenhum argumento seja provido você será perguntado dentro do script

Exemplos de Uso:
\t1.\tpython3 generate_milestones.py -n Mirai -c 1
\t2.\tpython3 generate_milestones.py Mirai 1
\t3.\tpython3 generate_milestones.py\n"""

MILESTONE_01_ABOUT = """Quantos filmes você já assistiu?

Bom, não precisa me responder mas imagino que você tenha assistido ao menos um filme...

E se existisse uma forma de você "guardar" esse filme? Pois então este será seu desafio, você irá programar uma biblioteca de filmes.

O seu objetivo é deixar da seguinte forma:

{INSERIR GIF}

---

Antes de começar eu gostaria que você fizesse algumas coisas:
- Crie um arquivo chamado `app.py`
- Escreva uma "DocString de Projeto/Teste"
- Documente quaisquer função que você criar usando DocStrings

O que seria essa "DocString de Projeto/Teste"?

é essencialmente um "cabeçalho" contendo informações como:
- Titulo (O Nome do Projeto)
- Objetivo (O motivo da criação do projeto)
- Descrição curta do projeto (entre 1 e 7 linhas)
- Lista de Tarefas (TODOs) (uma serie de etapas para concluir o projeto)
- Autor
- Data (Data de Inicio - Data de Finalização)

Aqui é um exemplo de um "cabeçalho" de outro projeto:

```py
\'\'\' Playground de Arvore Binária
    Esse programa foi escrito como desafio final no curso de Python.
    Um programa que gera, organiza, adiciona, exclui e exibe Arvores Binárias.

TODO:
    [x] - Criar os Nodes
    [x] - Implementar algoritmo base
    [x] - Menu
    [x] - Implementar algoritmos extras
    [x] - Implementar Formatação
    [ ] - Refatorar

AUTOR: Mirai
DATA: 12/10/21 - 14/10/21\'\'\'
```

---

## Dicas e Requerimentos

Como essa é sua primeira milestone eu irei colocar dicas e algumas coisas que eu quero que você faça

### Requerimentos

- Um menu usando `while` loop
- As opções devem ser divididas em funções

### Dicas

para limpar o console via python basta printar `\\033c`, ou adicionar esta linha de codigo:
```py
print("\\033c", end='')
```"""

MILESTONE_02_ABOUT = """Em progresso"""
MILESTONE_03_ABOUT = """Em progresso"""
MILESTONE_04_ABOUT = """Em progresso"""
MILESTONE_05_ABOUT = """Em progresso"""
MILESTONE_06_ABOUT = """Em progresso"""
MILESTONE_07_ABOUT = """Em progresso"""
MILESTONE_08_ABOUT = """Em progresso"""
MILESTONE_09_ABOUT = """Em progresso"""
MILESTONE_10_ABOUT = """Em progresso"""
MILESTONE_11_ABOUT = """Em progresso"""


class OsTypeError(Exception):
    """Error created for readability"""

    def __init__(self) -> None:
        Exception.__init__(self, "OS not detected")


def path_leaf(path_) -> str:
    """Return the basename of the path"""
    head, tail = split(path_)
    return tail or basename(head)


def get_cap(capnum: int):
    """Get the lessions chapter"""
    match capnum:
        case 1:
            milename = "FilmLibrary"
        case 2:
            milename = "BookLibrary"
        case 3:
            milename = "QuoteScraper"
        case 4:
            milename = "BookScraper"
        case 5:
            milename = "DiscordBot"
        case 6:
            milename = "TextEditor"
        case 7:
            milename = "PaintApp"
        case 8:
            milename = "Perceptron"
        case 9:
            milename = "TCPChatRoom"
        case 10:
            milename = "SecureTCPChatRoom"
        case 11:
            milename = "TorrentClient"
        case _:
            print("Cap name out of range")
            milename = input("Insira o numero da milestone: ")
    return milename, capnum


def get_user_values():
    """Get user Values"""
    _name = input("Insira seu nome(Nickname): ")
    _cp = input("Insira o numero da milestone: ")
    _chapter, _number = get_cap(int(_cp))
    return _name, _chapter, _number


def get_milestone_about(milestone_number: int = 0) -> str:
    """Função para retornar o sobre correspondente"""
    match milestone_number:
        case 1:
            milestone_about = MILESTONE_01_ABOUT
        case 2:
            milestone_about = MILESTONE_02_ABOUT
        case 3:
            milestone_about = MILESTONE_03_ABOUT
        case 4:
            milestone_about = MILESTONE_04_ABOUT
        case 5:
            milestone_about = MILESTONE_05_ABOUT
        case 6:
            milestone_about = MILESTONE_06_ABOUT
        case 7:
            milestone_about = MILESTONE_07_ABOUT
        case 8:
            milestone_about = MILESTONE_08_ABOUT
        case 9:
            milestone_about = MILESTONE_09_ABOUT
        case 10:
            milestone_about = MILESTONE_10_ABOUT
        case 11:
            milestone_about = MILESTONE_11_ABOUT
        case _:
            print("Cap name out of range")
            milestone_about = input("Insira o conteudo da milestone: ")

    return milestone_about


def print_help() -> None:
    """Prints the help message"""
    print(HELP_MESSAGE)
    sys.exit(0)


def mkfiles(
    filename: str = "",
    milestone_dir: str = "",
    milestone_name: str = "",
    milestone_number: int = "",
    milestone_about: str = "",
):
    """Creates the lessions files"""
    mdf = f"{filename}.md"
    pyf = f"{filename}.py"
    pyfpath = Path(path.join(milestone_dir, pyf))
    mdfpath = Path(path.join(milestone_dir, mdf))
    if not mdfpath.exists():
        with open(mdfpath, "w", encoding="UTF-8") as _f:
            _f.write(f"# {milestone_name}\n\n")
            _f.write(f"## Milestone {milestone_number:0>2}\n\n")
            _f.write(milestone_about)
    if not pyfpath.exists():
        with open(pyfpath, "w", encoding="UTF-8") as _:

            pass


def _get_system(basename_dir: str = "", _curr_pwd: str = "", name: str = ""):
    """Internal function to get system"""
    if system() == "Linux":
        if basename_dir != "Milestones":
            code_wd = f"{_curr_pwd}/Exercicios/Milestones"
        else:
            code_wd = _curr_pwd
        usr_dir = f"{code_wd}/{name}"
    elif system() == "Windows":
        if basename_dir != "Milestones":
            code_wd = f"{_curr_pwd}\\Exercicios\\Milestones"
        else:
            code_wd = _curr_pwd
        usr_dir = f"{code_wd}\\{name}"
    else:
        raise OsTypeError()

    return usr_dir


def main(args=None) -> None:
    """Main function"""
    if args is None:
        if len(argv) > 1:
            if str(argv[1]).lower():
                match str(argv[1]).lower():
                    case "--help":
                        print_help()
                    case "-h":
                        print_help()

                opts, targs = getopt(argv[1:], "n:c:", ["name=", "cap_num="])
                if opts:
                    name = opts[0][1]
                    cap, cap_number = get_cap(int(opts[1][1]))
                    mile_about = get_milestone_about(milestone_number=int(opts[1][1]))
                else:
                    name = targs[0]
                    cap, cap_number = get_cap(int(targs[1]))
                    mile_about = get_milestone_about(milestone_number=int(targs[1]))
        else:
            name, cap, cap_number = get_user_values()
            mile_about = get_milestone_about(milestone_number=int(cap_number))

        _curr_pwd = getcwd()
    basename_dir = path_leaf(_curr_pwd)

    usr_dir = _get_system(basename_dir=basename_dir, _curr_pwd=_curr_pwd, name=name)

    dirr = Path(usr_dir)
    filename = f"{cap}_{name}"

    if not dirr.exists():
        makedirs(usr_dir)
        cap_dir = path.join(usr_dir, cap)
        if not Path(cap_dir).exists():
            makedirs(cap_dir)
            mkfiles(
                filename=filename,
                milestone_number=cap_number,
                milestone_dir=cap_dir,
                milestone_name=cap,
                milestone_about=mile_about,
            )
        else:
            mkfiles(
                filename=filename,
                milestone_number=cap_number,
                milestone_dir=cap_dir,
                milestone_name=cap,
                milestone_about=mile_about,
            )
    else:
        cap_dir = path.join(usr_dir, cap)
        if not Path(cap_dir).exists():
            makedirs(cap_dir)
            mkfiles(
                filename=filename,
                milestone_number=cap_number,
                milestone_dir=cap_dir,
                milestone_name=cap,
                milestone_about=mile_about,
            )
        else:
            mkfiles(
                filename=filename,
                milestone_number=cap_number,
                milestone_dir=cap_dir,
                milestone_name=cap,
                milestone_about=mile_about,
            )


if __name__ == "__main__":
    main()
