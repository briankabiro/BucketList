class Bucket(object):
    def __init__(self, name, bucket=[]):
        self.name = name
        self.bucket = bucket

    def return_name(self):
        # print the name of the created user
        print(self.name)

    def add_item(self, item):
        self.bucket.append({"Id": len(self.bucket), "body": item})

    def update_item(self, Id, item):
        for i in self.bucket:
            if i['Id'] == Id:
                i['body'] == item

    def remove_item(self, Id):
        for i in self.bucket:
            if i['Id'] == Id:
                del i



