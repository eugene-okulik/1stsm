import allure
import requests
from endpoints.endpoint import Endpoint


class PutUpdateObject(Endpoint):

    @allure.step('Put update object')
    def make_put_update_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Patch update object')
    def make_patch_update_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
