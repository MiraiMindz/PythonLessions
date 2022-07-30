'''Script feito para padronizar e automatizar a criação de arquivos pertinentes as aulas

Notas: Talvez precise de refact mas funciona por agora então mais tarde eu faço
'''

from pathlib import Path
from ntpath import split, basename
from platform import system
from os import getcwd, makedirs, path
from sys import argv
from getopt import getopt


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self) -> None:
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self) -> None:
        return self.impl()


class _GetchUnix:
    def __init__(self) -> None:
        import tty
        import sys

    def __call__(self) -> None:
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


class OsTypeError(Exception):
    """Error created for readability"""

    def __init__(self) -> None:
        Exception.__init__(self, "OS not detected")


def path_leaf(path):
    h, t = split(path)
    return t or basename(h)


def get_cap(capnum: int):
    match capnum:
        case 1:
            capname = "IntroProgramacao"
        case 2:
            capname = "FundamentosI"
        case 3:
            capname = "FundamentosII"
        case 4:
            capname = "OrientacaoObjetoBase"
        case _:
            print("Cap name out of range")
            capname = input("Insira o nome do capitulo: ")
    return capname


def get_user_values():
    nm = input("Insira seu nome(Nickname): ")
    _cp = input("Insira o numero do capitulo: ")
    cp = get_cap(int(_cp))
    return nm, cp


def print_help():
    print("Uso:\n\tpython3 GenFile.py [-h] [-n] [-c] name cap_num\n\nUm script feito para automatizar/padronizar a criação de arquivos pertinentes as aulas.\n\nOptions:\n\t-h, --help\t\tExibe esta ajuda\n\t-n, --name\t\tEspecifica o nome\n \t-n, --cap_num\t\tEspecifica o numero do capitulo\n\nAs opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero do capitulo seguindo a ordem\nCaso nenhum argumento seja provido você será perguntado dentro do script\n\nExemplos de Uso:\n\t1.\tpython3 GenFile.py -n Mirai -c 1\n\t2.\tpython3 GenFile.py Mirai 1\n\t3.\tpython3 GenFile.py\n")
    exit()


def main(args=None) -> None:
    def mkfiles():
        if (not Path(path.join(cap_dir, f"{filename}.md")).exists()):
            with open(path.join(cap_dir, f"{filename}.md"), "w") as f:
                pass
        if (not Path(path.join(cap_dir, f"{filename}.py")).exists()):
            print("Gostaria de criar um arquivo em Python para acompanhar com codigo? (s/n)")
            resp = getch()
            if (resp.lower() == "s"):
                with open(path.join(cap_dir, f"{filename}.py"), "w") as f:
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
        if (basename_dir != "Code"):
            code_wd = f"{_curr_pwd}/Code"
        else:
            code_wd = _curr_pwd
        usr_dir = f"{code_wd}/{name}"
    elif (system() == "Windows"):
        if (basename_dir != "Code"):
            code_wd = f"{_curr_pwd}\\Code"
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


main()
