import allure
import requests
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    def __init__(self):
        self.object_id = None

    @allure.step('Delete Object')
    def delete_object(self):
        self.response = requests.delete(
            f'{self.url}/{self.object_id}'
        )
        return self.response.status_code
