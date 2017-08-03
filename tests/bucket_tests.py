import unittest
from app.models.bucket import Bucket

class TddinBucketlist(unittest.TestCase):
    def setUp(self):
        # create an object
        self.bucketlist = Bucket("bucketlist",1)

    def Test_bucketlist_created(self):
        # test if object is created
        self.assertEqual(self.bucketlist.name, "bucketlist")

    def Test_unique_id_created(self):
        # test if a unique id is created for each item
        self.bucketlist.add_item("one")
        self.assertNotEqual(self.bucketlist.count, 0)


    def Test_item_added_to_bucket(self):
        # test if an item is added to the object
        self.bucketlist.add_item("the winner by a knockout is")
        self.assertEqual(self.bucketlist.items[0]["body"],
                         "the winner by a knockout is")
    
    def Test_item_updated(self):
        self.bucketlist1 = Bucket("bucket", 2)
        self.bucketlist1.add_item('two')
        self.bucketlist1.update_item(0,'one')
    
    def Test_item_removed_from_bucket(self):
        # test if an item is removed from the bucket
        self.bucketlist.add_item("One")
        self.bucketlist.remove_item(0)
        self.assertNotIn(0, self.bucketlist.items)

    '''
    def Test_multiple_items_added(self):
        # test if multiple items are added to object
        self.bucketlist = Bucket('bucket',3)
        self.bucketlist.add_item("One")
        self.bucketlist.add_item("Two")
        print("this is self.bucketlist",self.bucketlist.items)
        self.assertEqual(len(self.bucketlist.items), 4)
'''

if __name__ == '__main__':
    unittest.main()