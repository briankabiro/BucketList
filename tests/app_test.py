import unittest
from app import app

class AppTest(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()
	# helper methods
	def signup(self,username,password):
		return self.client.post('/signup',
			data=dict(username=username, password=password),
			follow_redirects=True)
		
	def login(self,username,password):
		return self.client.post('/login',data=dict(username=username,password=password),follow_redirects=True)

	def logout(self):
		return self.client.post('/logout',follow_redirects=True)

	#Tests
	def Test_homepage(self):
		response = self.client.get('/')
		print('this is the respnse',response)
		self.assertEqual(response.status,'200 OK')

	def Test_signup_page(self):
		response = self.client.get('/signup')
		self.assertEqual(response.status,'200 OK')


	def Test_login_page(self):
		response = self.client.get('/login')
		self.assertEqual(response.status, '200 OK')

'''
	def Test_User_is_Registered(self):
		response = self.signup("lee","12345")
		self.assertEqual(session['username'], 'lee')

	def Test_logout(self):
		self.signup('lee','12345')
		return self.client.post('/logout', follow_redirects=True)
'''