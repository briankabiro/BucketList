import unittest
from models.bucket import Bucket
from models.user import User


class TddinBucketlist(unittest.TestCase):
    def setUp(self):
        # create an object
        self.bucketlist = Bucket("bucketlist")

    def Test_bucketlist_created(self):
        # test if object is created
        self.assertEqual(self.bucketlist.name, "bucketlist")

    def Test_item_added_to_bucket(self):
        # test if an item is added to the object
        self.bucketlist.add_item("the winner by a knockout is")
        self.assertEqual(self.bucketlist.bucket[0]["body"],
                         "the winner by a knockout is")

    def Test_item_removed_from_bucket(self):
        # test if an item is removed from the bucket
        self.bucketlist.add_item("One")
        self.bucketlist.remove_item(0)
        self.assertNotIn(0, self.bucketlist.bucket)


    def Test_multiple_items_added(self):
        # test if multiple items are added to object
        self.bucketlist.bucket = []
        self.bucketlist.add_item("One")
        self.bucketlist.add_item("Two")
        self.assertEqual(len(self.bucketlist.bucket), 2)


class TddinUser(unittest.TestCase):
    def setUp(self):
        # create a User object
        self.user = User("user", "1234")

    def Test_user_created(self):
        # test if the user has been created
        self.assertEqual(self.user.name, "user")


if __name__ == '__main__':
    unittest.main()