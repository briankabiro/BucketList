import unittest
from app.app import Bucketlist, User

class TddinBucketlist(unittest.TestCase):
	def setUp(self):
		self.bucketlist = Bucketlist("bucketlist")

	def test_bucketlist_created(self):
		self.assertEqual(self.bucketlist.name,"bucketlist")

	def test_item_added_to_bucket(self):
		self.bucketlist.add_item("the winner by a knockout is")
		self.assertEqual(self.bucketlist.bucket[0]["body"],"the winner by a knockout is")
	
	def test_item_removed_from_bucket(self):
		self.bucketlist.add_item("One")
		self.bucketlist.remove_item(0)
		self.assertNotIn(0,self.bucketlist.bucket)

	def test_delete_method_deletes_bucket_list(self):
		self.assertTrue(self.bucketlist.__del__())
		
	def test_multiple_items_added_to_bucket(self):
		self.bucketlist.bucket = []
		self.bucketlist.add_item("One")
		self.bucketlist.add_item("Two")
		self.assertEqual(len(self.bucketlist.bucket),2)

class TddinUser(unittest.TestCase):
	def setUp(self):
		self.user = User("user","1234")

	def test_user_created(self):
		self.assertEqual(self.user.name,"user")
		
	def test_user_logged_out(self):
		self.assertTrue(self.user.__del__())
if __name__ == '__main__':
	unittest.main()