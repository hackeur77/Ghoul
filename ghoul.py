# -*- coding: utf-8 -*-

# made by billythegoat356

# https://github.com/billythegoat356/Ghoul

# <3



from pyfade import Fade, Colors
from pycenter import center
from terminaltables import DoubleTable
from requests import get, post


from os import name, system
from random import shuffle
from base64 import b64decode as bd
from webbrowser import open as openb


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


def mkmodes():
    l = get(url + "/len").text
    modes = {
            "+": "Ghoul - {} victims".format(l),
            "1": "Discover",
            "2": "Search by username",
            "3": "Add data to username"}

    return maketable(modes, "Modes").table




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


def ui(spaces):
    clear()

    print(Fade.Vertical(Colors.white_to_black, center(banner)))
    Col.vdgprint(center(author))
    print(spaces)


def menu(mode: int = 0, username: str = False):
    ui("\n")
    if mode == 0:
        modestable = mkmodes()
        Col.dgprint(center(modestable))

    print("\n\n")

    if mode == 0:

        mode = Col.ginput("-> ")

        if mode == '+':
            openb("https://github.com/billythegoat356/Ghoul")
            return menu()

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
        return discover()
    elif mode == 2:
        return search(username)

    elif mode == 3:
        return add()

def discover():
    Col.gprint("Getting usernames...")

    usernames = get(url + "/all").text.splitlines()
    shuffle(usernames)
    m = min(len(usernames), 10)
    usr = {"+": "{} random victims out of {}".format(m, len(usernames))}
    for a, b, _, in zip(range(1,len(usernames)+1), usernames, range(m)):
        usr[a] = b
    ui("\n\n")
    Col.dgprint(center(maketable(usr, "Usernames").table))
    choice = Col.ginput("-> ")
    try:
        choice = int(choice)
    except ValueError:
        return menu()
    if choice not in range(1, m+1):
        return menu()
    return menu(mode=2, username=usr[choice])

def search(username):
    username = Col.ginput("Username [a-z|0-9] -> ") if username is False else username
    if username == '':
        return menu()

    r = post(url + "/get", json={"username": username}).text

    Col.dginput(center(makebox(r)))

def add():

    username = Col.ginput("Username [a-z|0-9] -> ")
    if username == '':
        return menu()
    data = Col.ginput("Data -> ")
    if data == '':
        return menu()

    r = post(url + "/add", json = {"username": username, "data": data}).text

    Col.dginput(center(makebox(r)))



if __name__ == '__main__':
    while True:
        menu()
