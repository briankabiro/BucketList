import unittest
from app.app import Bucketlist

class TddinBucketlist(unittest.TestCase):
	def setUp(self):
		self.bucketlist = Bucketlist("bucketlist")

	def test_bucketlist_created(self):
		self.assertEqual(self.bucketlist.name,"bucketlist")

	def test_item_added_to_bucket(self):
		self.bucketlist.add_item("the winner by a knockout is")
		self.assertEqual(self.bucketlist.bucket[0],"the winner by a knockout is")
	
	def test_item_removed_from_bucket(self):
		self.bucketlist.add_item("One")
		self.bucketlist.remove_item(0)
		self.assertNotIn(0,self.bucketlist.bucket)

	def test_delete_method_deletes_bucket_list(self):
		self.assertTrue(self.bucketlist.__del__())
		
	def test_multiple_items_added_to_bucket(self):
		self.bucketlist.add_item("One")
		self.bucketlist.add_item("Two")
		self.assertEqual(len(self.bucketlist.bucket),2)
		
if __name__ == '__main__':
	unittest.main()