import unittest
from app import app

class AppTest(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()

	def Test_homepage(self):
		response = self.client.get('/')
		print('this is the respnse',response)
		self.assertEqual(response.status,'200 OK')

	def register(self,username,password):
		return self.client.post('/register',
			data=dict(username=username, password=password),
			follow_redirects=True)
		
	def login(self,username,password):
		return self.client.post('/login',data=dict(username=username,password=password),follow_redirects=True)

	def logout(self):
		return self.client.post('/logout',follow_redirects=True)
'''
	def Test_Register_Page(self):
		response = self.client.get('/register/')
		print("this is the response",response)
		self.assertEqual(response.status,'200 OK')

	def Test_User_is_Registered(self):
		response = self.register("lee","12345")
		self.assertEqual(response.status_code,'200 OK')

	def Test_logout(self):
		self.register('lee','12345')
		return self.client.post('/logout', follow_redirects=True)
		'''