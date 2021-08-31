from flask import Flask, redirect, request

from src.database import Database, data


app = Flask("Ghoul")
port = 8502


@app.route('/')
def main():
    return redirect("https://github.com/billythegoat356/Ghoul")


@app.route("/all", methods=['GET'])
def all():
    return Database.getall()

@app.route("/len", methods=['GET'])
def glen():
    return str(len(data))


@app.route("/get", methods=['POST'])
def get():

    json = request.get_json()

    if json is None or "username" not in json or len(json) != 1 or type(json['username']) != str:
        return 'invalid json', 400

    username = json['username']

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

    if len(username) > 20:
        return "maximum length of username", 400

    if len(data) > 100:
        return 'maximum length of data', 400

    Database.add(username)

    return "done"


app.run(host='0.0.0.0', port=port)
