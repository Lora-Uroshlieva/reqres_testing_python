import requests


class ReqresRestApi:
    def __init__(self):
        self.host = 'reqres.in/api'
        self.url = "https://reqres.in/api/"

    def get_users(self):
        response = requests.get(self.url + "users/")
        return response.json()

    def get_user(self, user_id=1):
        response = requests.get(self.url + "users/" + str(user_id))
        return response.json()

    def create_user(self, name, job):
        data = {
    "name": "morpheus",
    "job": "leader"
}
        response = requests.post(self.url, data)
        print(data)
        print(response)
        # return response.json()

    def update_user(self, job):
        pass
        # response = requests.put(self.url, )
        # return response.json()

    def delete_user(self):
        pass

