import unittest
from api_helper import ReqresRestApi

api = ReqresRestApi()


class UserTest(unittest.TestCase):

    # def test_get_users(self):
    #     users = api.get_users()['data']
    #     for user in users:
    #         self.assertNotEqual(user['first_name'], None)
    #
    # def test_get_user(self):
    #     user = api.get_user(6)
    #     print(user)
    #     self.assertEqual(user['data']['id'], 6)

    # @unittest.skip
    def test_create_user(self):
        user = api.create_user('John Snow', 'King of the North')
        print(user)


if __name__ == "__main__":
    unittest.main(verbosity=2)
