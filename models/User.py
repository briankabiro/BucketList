class User(object):
    #create new user
    def __init__(self, name="", password=""):
        self.name = name
        self.password = password

    def return_name(self):
        return self.name

    def __del__(self):
        return True
