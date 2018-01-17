import requests
import shutil


# noinspection PyMethodMayBeStatic
class ReqresRestApi:
    def __init__(self):
        self.host = "reqres.in/api"
        self.url = "https://reqres.in/api/"

    def get_users(self):
        response = requests.get(self.url + "users/")
        return response.json()

    def get_user(self, user_id=1):
        response = requests.get(self.url + "users/" + str(user_id))
        return response.json()

    def create_user(self, name, job):
        data = {
            "name": name,
            "job": job
                }
        response = requests.post(self.url + "users", data=data)
        return response

    def update_user(self, user):
        response = requests.put(self.url + "users/" + str(user["id"]),
                                data=user)
        return response

    def delete_user(self, user):
        return requests.delete(self.url + "users/" + str(user["id"]))

    def get_file(self, url, abs_file_path):
        response = requests.get(url, stream=True)
        with open(abs_file_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return response
