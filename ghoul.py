# -*- coding: utf-8 -*-

# made by billythegoat356

# https://github.com/billythegoat356/Ghoul

# <3



from pyfade import Fade, Colors
from pycenter import center
from terminaltables import DoubleTable
from requests import get, post


from os import name, system
from base64 import b64decode as bd



def clear(): system("cls" if name == 'nt' else "clear")


if name == 'nt':
    system("mode 160, 40")
    system("title Ghoul")


def maketable(dictionnary: dict, title: str):
    table = [(f" {str(key)}" if len(str(key)) == 1 else str(key), value)
             for key, value in dictionnary.items()]
    return DoubleTable(table_data=table, title=title)

def makebox(content: str):
    l = 0
    lines = content.splitlines()
    for a in lines:
        if len(a) > l:
            l = len(a)
    if l %2 == 1:
        l += 1
    box = "__" + ("_" * l) + "__\n"
    box += "| " + (" " * int(l / 2)) + (" " * int(l / 2)) + " |\n"
    for line in lines:
        box += "| " + line + (" " * int((l - len(line)))) + " |\n"
    box += "|_" + ("_" * l) + "_|\n"

    return box


modes = {
        "+": "Ghoul",
        "1": "Discover",
        "2": "Search by username",
        "3": "Add data to username"}

modestable = maketable(modes, "Modes").table

def printable():
    return Col.dgprint(center(modestable))


class Col:
    colors = {"red": "\033[38;2;255;0;0m",
              "gray": "\033[38;2;150;150;150m",
              "darkgray": "\033[38;2;100;100;100m",
              "verydarkgray": "\033[38;2;50;50;50m",
              "white": "\033[38;2;255;255;255m"}

    red = colors['red']

    gray = colors['gray']

    darkgray = colors['darkgray']

    verydarkgray = colors['verydarkgray']

    white = colors['white']

    def error(text):
        return input(Col.red + "\n" + text + Col.white)
    
    def gprint(text):
        return print(Col.gray + text + Col.white)
    
    def ginput(text):
        return input(Col.gray + text + Col.white)

    def dgprint(text):
        return print(Col.darkgray + text + Col.white)

    def dginput(text):
        return input(Col.darkgray + text + Col.white)

    def vdgprint(text):
        return print(Col.verydarkgray + text + Col.white)

    def vdginput(text):
        return input(Col.verydarkgray + text + Col.white)


banner = """
                       ___                
.+'|=|`+. .+'| |`+. .+'   `+. .+'| |`+. .+'|
|  | \__| |  | |  | |   _   | |  | |  | |  |
|  |      |  |=|  | |  | |  | |  | |  | |  |
|  | |`+. |  | |  | |  | |  | |  | |  | |  |
|  | `| | |  | |  | |  |_|  | |  |_|  | |  |    .
|  |__| | |  | |  | |       | |       | |  | .+'|
`+.___.+' `+.| |..| `+.___.+' `+.___.+' `+.___.+'
"""[1:]

author = "\ \ \ {} / / /".format(bd("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))


url = "https://Ghoul.billythegoat356.repl.co"


def menu(mode: int = 0):
    ui("\n")
    if mode == 0:
        printable()

    print("\n\n")

    if mode == 0:

        mode = Col.ginput("-> ")

        try:
            mode = int(mode)
        except ValueError:
            Col.error("Invalid choice!")
            return menu()

        if mode not in [1, 2, 3]:
            Col.error("Invalid choice!")
            return menu()

        return menu(mode=mode)

    elif mode == 1:
        Col.gprint("Getting usernames...")

        usernames = get(url + "/all").text
        ui("\n\n")
        Col.dginput(center(makebox(usernames)))


    elif mode == 2:
        username = Col.ginput("Username -> ")
        r = post(url + "/get", json={"username":username}).text


        Col.dginput(center(makebox(r)))

    elif mode == 3:

        username = Col.ginput("Username -> ")
        data = Col.ginput("Data -> ")

        r = post(url + "/add", json = {"username":username, "data":data}).text

        Col.dginput(center(makebox(r)))

def ui(spaces):
    clear()

    print(Fade.Vertical(Colors.white_to_black, center(banner)))
    Col.vdgprint(center(author))
    print(spaces)


if __name__ == '__main__':
    while True:
        menu()