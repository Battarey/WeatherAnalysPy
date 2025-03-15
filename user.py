class User:
    def __init__(self, nick):
        self.nick = nick
        self.is_authenticated = False
        pass

    def login(self):
        self.is_authenticated = True
        print(f"{self.nick}")

    def getNick(self):
        return self.nick
    
    # def check_status(self):
    #     return True if self.is_authenticated else False

    def check_status(self):
        return self.is_authenticated  # Возвращаем True или False
