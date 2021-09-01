from flask import Flask, redirect, request

from src.database import Database

from googletrans import Translator


translator = Translator()

translation = translator.translate("ghoul")


# pip install googletrans==3.1.0a0


app = Flask("Ghoul")
port = 8502


invalid = """\/:*?"<>|’!.&%"'"""


def check(username: str):
    return "".join(a.lower() for a in username.strip() if a not in invalid)


def verify1(data: str):
    files = Database._getall()
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            if data in f.read():
                return False
    return True

def verify2(data: str):

    data = data.split()
    l = len(data)
    r = sum(translator.translate(i).text == i for i in data)
    return r <= l/2



@app.route('/')
def main():
    return redirect("https://github.com/billythegoat356/Ghoul")


@app.route("/len", methods=['GET'])
def glen():
    return Database.getlen()




@app.route("/all", methods=['GET'])
def all():
    return Database.getall()


@app.route("/get", methods=['POST'])
def get():

    json = request.get_json()

    if json is None or "username" not in json or len(json) != 1 or type(json['username']) != str:
        return 'invalid json', 400

    username = json['username']
    username = username.lower()

    username = check(username)

    usr = Database.get(username)
    if usr is False:
        return 'username not found', 403

    else:
        return usr


@app.route("/add", methods=['POST'])
def add():

    json = request.get_json()

    if json is None or "username" not in json or "data" not in json or len(json) != 2 or type(json['username']) != str or type(json['data']) != str:
        return 'invalid json', 400

    username = json['username']
    data = json['data']

    username = username.lower()

    username = check(username)

    if len(data.split()) < 5:
        return "data has to be longer than 5", 400

    if not verify1(data):
        return "try to change your data a bit, since its already used in another username", 400
    
    if not verify2(data):
        return "your data contains too many words that are from an unknown language, please try to write corectly x)", 400

    if len(username) > 20:
        return "maximum length of username", 400

    if len(data) > 100:
        return 'maximum length of data', 400

    Database.add(username, data)

    return "done"


app.run(host='0.0.0.0', port=port)
