'''Script feito para padronizar e automatizar a criação de arquivos pertinentes as aulas

Notas: Talvez precise de refact mas funciona por agora então mais tarde eu faço'''

from pathlib import Path
from ntpath import split, basename
from platform import system
from os import getcwd, makedirs, path
from sys import argv
from getopt import getopt

help_msg = '''Uso:
\tpython3 GenFile.py [-h] [-n] [-c] name cap_num

Um script feito para automatizar/padronizar a criação de arquivos pertinentes as aulas.

Options:
\t-h, --help\t\tExibe esta ajuda
\t-n, --name\t\tEspecifica o nome
\t-c, --cap_num\t\tEspecifica o numero do capitulo

As opções [-n] e [-c] são opcionais, você pode omiti-las caso insira o nome e o numero do capitulo seguindo a ordem
Caso nenhum argumento seja provido você será perguntado dentro do script

Exemplos de Uso:
\t1.\tpython3 GenFile.py -n Mirai -c 1
\t2.\tpython3 GenFile.py Mirai 1
\t3.\tpython3 GenFile.py\n'''



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
            capname = "IntroProgramacao"
        case 2:
            capname = "FundamentosI"
        case 3:
            capname = "FundamentosII"
        case 4:
            capname = "OrientacaoObjetoBase"
        case 5:
            capname = "Erros"
        case 6:
            capname = "Arquivos"
        case 7:
            capname = "Databases"
        case 8:
            capname = "TypeHint"
        case 9:
            capname = "FuncNativasAvancadas"
        case 10:
            capname = "DesenvAvancado"
        case 11:
            capname = "WebScraping"
        case 12:
            capname = "AutomacaoSelenium"
        case 13:
            capname = "AsyncDev"
        case 14:
            capname = "VirtualEnv"
        case 15:
            capname = "WebDev"
        case 16:
            capname = "APIs"
        case 17:
            capname = "Decorators"
        case 18:
            capname = "OrientacaoObjetoAvancada"
        case 19:
            capname = "UnitTests"
        case 20:
            capname = "CienciaDados"
        case 21:
            capname = "AlgoritmosEstruturaDadosMachineLearning"
        case 22:
            capname = "Bibliotecas"
        case 23:
            capname = "DocumentacaoBoasPraticas"
        case 24:
            capname = "RedesSoquetes"
        case 25:
            capname = "Criptografia"
        case 26:
            capname = "CyberSecHackingEtico"
        case 27:
            capname = "ProgramacaoAvancada"
        case 28:
            capname = "GameDev"
        case _:
            print("Cap name out of range")
            capname = input("Insira o numero do capitulo: ")
    return capname


def get_user_values() -> str:
    """Get user Values"""
    nm = input("Insira seu nome(Nickname): ")
    _cp = input("Insira o numero do capitulo: ")
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


if (__name__ == "__main__"):
    main()
