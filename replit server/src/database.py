from pydifference import Difference


data = {"billy": "hacker"}


class Database:
    def get(username: str):
        r = Difference.getfromlist(username, list(data.keys()), diff=2, max=1)
        if len(r) == 1:
            r = r[0]
            return "Username: {}\n\n".format(r) + data[r]
        return False

    def add(username: str, content: str):
        r = Database.get(username)
        c = "" if r is False else r + "\n\n"
        data[username] = c + content
        return True

    def getall():
        return "\n".join(data.keys())
