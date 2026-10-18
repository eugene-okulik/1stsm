import requests
import pytest


url = 'http://objapi.course.qa-practice.com/object'


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
    response = requests.post(url, headers=headers, json=body)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'{url}/{obj_id}')


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


def test_get_all_objects():
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.critical
@pytest.mark.parametrize("name", ["alfa", "bravo", "delta"])
def test_new_object(name):
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": name,
        "data": {
            "color": "blue",
            "size": "small"
        }
    }
    response = requests.post(url, headers=headers, json=body)
    obj_id = response.json()['id']

    try:
        assert response.json()['name'] == name
        assert response.status_code == 200

    finally:
        requests.delete(f'{url}/{obj_id}')


def test_get_object(object_id):
    response = requests.get(f'{url}/{object_id}')
    assert response.status_code == 200
    assert response.json()['name'] == 'tsm object'


@pytest.mark.medium
def test_put_object(object_id):
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "full update object",
        "data": {
            "color": "red",
            "size": "big"
        }
    }
    response = requests.put(f'{url}/{object_id}', headers=headers, json=body)
    response_data = response.json()
    assert response_data['name'] == 'full update object'
    assert response.status_code == 200


def test_patch_object(object_id):
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "partially updated object"
    }
    response = requests.patch(f'{url}/{object_id}', headers=headers, json=body)
    response_data = response.json()
    assert response_data['name'] == 'partially updated object'
    assert response.status_code == 200


def test_delete_object(object_id):
    response = requests.delete(f'{url}/{object_id}')
    assert response.status_code == 200

    response = requests.get(f'{url}/{object_id}')
    assert response.status_code == 404
