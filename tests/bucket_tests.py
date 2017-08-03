import unittest
from app.models.bucket import Bucket


class TddinBucketlist(unittest.TestCase):
    def setUp(self):
        # function that runs before each test
        self.bucket = Bucket('One', 1)

    def Test_bucketlist_created(self):
        # test if object is created
        self.assertEqual(self.bucket.return_name(), "One")

    def Test_bucket_name_updated(self):
        self.bucket.update_name('Two')
        self.assertEqual(self.bucket.name, 'Two')

    def Test_unique_id_created(self):
        # test if a unique id is created for each item
        self.bucket.add_item("one")
        self.assertNotEqual(self.bucket.count, 0)

    def Test_item_added_to_bucket(self):
        # test if an item is added to the object
        self.bucket.add_item("the winner by a knockout is")
        self.assertEqual(self.bucket.items[0]["body"],
                         "the winner by a knockout is")
        self.bucket.remove_item("0")

    def Test_item_updated(self):
        # test if the body of an item in bucket list is updated
        self.bucket.add_item('one')
        self.bucket.update_item("0", "two")
        print('tis is self.bucket', self.bucket.items)
        self.assertEqual(self.bucket.items[0]["body"], 'two')
        self.bucket.remove_item("0")

    def Test_item_removed_from_bucket(self):
        # test if an item is removed from the bucket
        print('this is self.bucket.items', self.bucket.items)
        self.bucket.add_item('sleep')
        self.bucket.remove_item("0")
        self.assertEqual(0, len(self.bucket.items))

    def Test_multiple_items_added(self):
        # test if multiple items are added to object
        self.bucket.add_item("One")
        self.bucket.add_item("Two")
        print("this is self.bucket", self.bucket.items)
        self.assertEqual(len(self.bucket.items), 2)


if __name__ == '__main__':
    unittest.main()