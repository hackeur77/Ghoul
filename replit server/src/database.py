from pydifference import Difference


data = {"billy": "hacker"}

class Database:
    def get(username: str):
        r = Difference.getfromlist(username, list(data.keys()), diff=2, max=1)
        if len(r) == 1:
            r = r[0]
            return data[r]
        return False


    def add(username: str, content: str):
        r = Database.get(username)
        c = "" if r is False else r
        data[username] = c + content
        return True



    def getall():
        return "\n".join(usr + ": " + dt for usr, dt in data.items())