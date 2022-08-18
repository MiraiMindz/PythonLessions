'''Script feito para padronizar e automatizar a criação de arquivos pertinentes as milestones [igual ao arquivo das aulas]

Notas: Talvez precise de refact mas funciona por agora então mais tarde eu faço'''

from pathlib import Path
from ntpath import split, basename
from platform import system
from os import getcwd, makedirs, path
from sys import argv
from getopt import getopt

help_msg = '''Uso:
\tpython3 GenMilestones.py [-h] [-n] [-c] name milestone_num

Um script feito para automatizar/padronizar a criação de arquivos pertinentes as milestones.

Options:
\t-h, --help\t\tExibe esta ajuda
\t-n, --name\t\tEspecifica o nome
\t-c, --milestone_num\tEspecifica o numero da milestone

As opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero da milestone seguindo a ordem
Caso nenhum argumento seja provido você será perguntado dentro do script

Exemplos de Uso:
\t1.\tpython3 GenMilestones.py -n Mirai -c 1
\t2.\tpython3 GenMilestones.py Mirai 1
\t3.\tpython3 GenMilestones.py\n'''



class OsTypeError(Exception):
    """Error created for readability"""

    def __init__(self) -> None:
        Exception.__init__(self, "OS not detected")


def path_leaf(path) -> str:
    """Return the basename of the path"""
    h, t = split(path)
    return t or basename(h)


def get_cap(capnum: int) -> str:
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
    return milename


def get_user_values() -> str:
    """Get user Values"""
    nm = input("Insira seu nome(Nickname): ")
    _cp = input("Insira o numero da milestone: ")
    cp = get_cap(int(_cp))
    return nm, cp


def print_help() -> None:
    """Prints the help message"""
    print(help_msg)
    exit()


def main(args=None) -> None:
    """Main function"""
    def mkfiles():
        """Creates the lessions files"""
        mdf = f"{filename}.md"
        pyf = f"{filename}.py"
        pyfpath = Path(path.join(cap_dir, pyf))
        mdfpath = Path(path.join(cap_dir, mdf))
        if (not mdfpath.exists()):
            with open(mdfpath, "w") as f:
                pass
        if (not pyfpath.exists()):
            resp = input("Gostaria de criar um arquivo em Python para acompanhar com codigo? (s/n) ")
            if (resp.lower() == "s"):
                with open(pyfpath, "w") as f:
                    pass

    if (args is None):
        if len(argv) > 1:
            if str(argv[1]).lower():
                match str(argv[1]).lower():
                    case "--help":
                        print_help()
                    case "-h":
                        print_help()

                opts, targs = getopt(argv[1:], 'n:c:', ["name=", "cap_num="])
                if (opts):
                    name = opts[0][1]
                    cap = get_cap(int(opts[1][1]))
                else:
                    name = targs[0]
                    cap = get_cap(int(targs[1]))
        else:
            name, cap = get_user_values()

    _curr_pwd = getcwd()
    basename_dir = path_leaf(_curr_pwd)

    if (system() == "Linux"):
        if (basename_dir != "Milestones"):
            code_wd = f"{_curr_pwd}/Exercicios/Milestones"
        else:
            code_wd = _curr_pwd
        usr_dir = f"{code_wd}/{name}"
    elif (system() == "Windows"):
        if (basename_dir != "Milestones"):
            code_wd = f"{_curr_pwd}\\Exercicios\\Milestones"
        else:
            code_wd = _curr_pwd
        usr_dir = f"{code_wd}\\{name}"
    else:
        raise OsTypeError()

    dirr = Path(usr_dir)
    filename = f"{cap}_{name}"

    if (not dirr.exists()):
        makedirs(usr_dir)
        cap_dir = path.join(usr_dir, cap)
        if (not Path(cap_dir).exists()):
            makedirs(cap_dir)
            mkfiles()
        else:
            mkfiles()
    else:
        cap_dir = path.join(usr_dir, cap)
        if (not Path(cap_dir).exists()):
            makedirs(cap_dir)
            mkfiles()
        else:
            mkfiles()


if (__name__ == "__main__"):
    main()
