import unittest
import datetime
import os
from api_helper import ReqresRestApi

api = ReqresRestApi()


class UserTest(unittest.TestCase):

    def test_get_users(self):
        users = api.get_users()["data"]
        for user in users:
            self.assertNotEqual(user["first_name"], None)

    def test_get_user(self):
        user = api.get_user(6)
        self.assertEqual(user["data"]["id"], 6)

    def test_create_user(self):
        user = {"name": "John Snow", "job": "King of the North"}
        new_user = api.create_user(user["name"], user["job"])
        self.assertEqual(new_user.status_code, 201)
        new_user = new_user.json()
        for key in user:
            self.assertEqual(user[key], new_user[key])
        self.assertEqual(datetime.datetime.now().strftime("%Y-%m-%d"), new_user["createdAt"][0:10])

    def test_update_user(self):
        user = api.get_user(5)["data"]
        user["first_name"] = "Ivan"
        user["last_name"] = "Ivanov"
        updated_user = api.update_user(user)
        self.assertEqual(updated_user.status_code, 200)
        updated_user = updated_user.json()
        self.assertEqual(user["first_name"], updated_user["first_name"])
        self.assertEqual(user["last_name"], updated_user["last_name"])
        self.assertEqual(datetime.datetime.now().strftime("%Y-%m-%d"), updated_user["updatedAt"][0:10])

    def test_delete_user(self):
        user = api.get_users()["data"][0]
        response = api.delete_user(user)
        self.assertEqual(response.status_code, 204)

    def test_load_user_avatar(self):
        user = api.get_user(1)["data"]
        url_avatar = user['avatar']
        avatar_directory = os.path.dirname(__file__) + os.path.sep + 'images'
        if not os.path.isdir(avatar_directory):
            os.makedirs(avatar_directory)
        file_extension = url_avatar.split('.')[-1]
        file_name = user['first_name'] + "_" + user["last_name"] + '.' + file_extension
        path = avatar_directory + os.path.sep + file_name
        response = api.get_file(url_avatar, path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.isfile(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
