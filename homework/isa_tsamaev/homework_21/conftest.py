import pytest
import requests
import allure

URL = 'http://objapi.course.qa-practice.com/object'


@pytest.fixture()
def object_id():
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "tsm object",
        "data": {
            "color": "blue",
            "size": "small"
        }
    }
    with allure.step('Create test object'):
        response = requests.post(URL, headers=headers, json=body)
        obj_id = response.json()['id']
    yield obj_id
    with allure.step('Delete test object'):
        requests.delete(f'{URL}/{obj_id}')


@pytest.fixture(autouse=True)
def before_after_text():
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope='session', autouse=True)
def start_end_text():
    print('Start testing')
    yield
    print('Testing completed')