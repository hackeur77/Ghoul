from os import listdir

from datetime import datetime


def removesuffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def get_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y - %H:%M:%S:\n\n")


class Database:
    def get(username: str):
        for file in listdir('src/db'):
            file = removesuffix(file, '.txt')
            if file == username:
                with open('src/db/'+file+'.txt', 'r', encoding='utf-8') as f:
                    return f.read()
        return False

    def add(username: str, content: str):
        r = Database.get(username)
        c = "" if r is False else r + "\n\n\n"
        with open('src/db/'+username+'.txt', 'w', encoding='utf-8') as f:
            f.write(c + get_time() + content)
        return True

    def getall():
        r = [removesuffix(file, '.txt') for file in listdir('src/db')]

        return "\n".join(r)