from locust import task, HttpUser
import random


class ObjectUser(HttpUser):
    object_id = None
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "tsm object",
        "data": {
            "color": "blue",
            "size": "small"
        }
    }

    def on_start(self):
        response = self.client.post("/object", json=self.body, headers=self.headers)
        self.object_id = response.json()['id']

    @task(1)
    def get_all_objects(self):
        self.client.get(
            "/object",
            headers={"Content-Type": "application/json"}
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([self.object_id, 1])}',
            headers={"Content-Type": "application/json"}
        )

    def on_stop(self):
        self.client.delete(
            f"/object/{self.object_id}",
            headers=self.headers
        )
