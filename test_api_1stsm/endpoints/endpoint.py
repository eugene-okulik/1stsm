import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Verify object name')
    def check_object_name(self, name):
        assert self.json['name'] == name

    @allure.step('Check status code is 200')
    def check_status_code(self):
        assert self.response.status_code == 200
