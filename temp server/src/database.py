fdata = {"billy": "bg"}


class Database:
    def get(username: str):
        if username in fdata:
          return fdata[username]
        return False

    def add(username: str, content: str):
        r = Database.get(username)
        c = "" if r is False else r + "\n\n"
        fdata[username] = c + content
        return True

    def getall():
        return "\n".join(fdata.keys())
    
    def getlen():
        return str(len(fdata))