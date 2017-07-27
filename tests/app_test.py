import unittest
import app
__import__('Bucket-List')

class AppTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def Test_homepage(self):
		rv = self.app.get('/')
		self.assert_template_used('index.html')	

	def Test_login(self):
		pass