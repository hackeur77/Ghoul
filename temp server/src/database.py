data = {"billy": "hacker"}


class Database:
    def get(username: str):
        if username in data:
          return data[username]
        return False

    def add(username: str, content: str):
        r = Database.get(username)
        c = "" if r is False else r + "\n\n"
        data[username] = c + content
        return True

    def getall():
        return "\n".join(data.keys())