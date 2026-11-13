import allure
import requests
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get all object')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Get one object')
    def get_one_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.response
