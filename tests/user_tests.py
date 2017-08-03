import unittest
from app.models.user import User

class TddinUser(unittest.TestCase):
    def setUp(self):
        # create a User object
        self.user = User("user", "1234", 1)

    def Test_user_created(self):
        # test if the user has been created
        self.assertEqual(self.user.name, "user")

    def Test_user_name_returned(self):
    	self.assertEqual(self.user.return_name(),'user')