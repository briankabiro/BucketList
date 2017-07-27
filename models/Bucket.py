class Bucket(object):
    def __init__(self, name, Id, items=[], count=0):
        self.name = name
        self.items = items
        self.Id = Id
        self.count = count

    def return_name(self):
        # print the name of the created user
        return self.name

    def update_name(self, new_title):
        self.name = new_title

    def add_item(self, item):
        self.items.append({"Id": self.count, "body": item})
        self.count += 1

    def update_item(self, Id, item):
        for i in self.items:
            if str(i['Id']) == Id:
                i['body'] = item

    def remove_item(self, Id):
        for i in self.items:
            if str(i['Id']) == Id:
                self.items.remove(i)
