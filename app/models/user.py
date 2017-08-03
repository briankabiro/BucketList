class User(object):
    #create new user
    def __init__(self, name, password, Id):
        self.name = name
        self.password = password
        self.Id = Id

    def return_name(self):
        return self.name