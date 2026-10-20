import requests
import pytest
import allure


URL = 'http://objapi.course.qa-practice.com/object'


@allure.epic('Object API')
@allure.feature('Object Retrieval')
@allure.story('Get all objects')
@allure.title('Получение списка всех объектов')
def test_get_all_objects():
    with allure.step('Send GET request to retrieve all objects'):
        response = requests.get(URL)
    with allure.step('Verify response status code'):
        assert response.status_code == 200


@allure.epic('Object API')
@allure.feature('Object Creation')
@allure.story('Create object with different names')
@allure.title('Создание объекта с именем: {name}')
@pytest.mark.critical
@pytest.mark.parametrize("name", ["alfa", "bravo", "delta"])
def test_new_object(name):
    body = {
        "name": name,
        "data": {
            "color": "blue",
            "size": "small"
        }
    }
    with allure.step(f'Create object with name: {name}'):
        response = requests.post(URL, json=body)
        obj_id = response.json()['id']

    try:
        with allure.step('Verify object name'):
            assert response.json()['name'] == name
        with allure.step('Verify response status code'):
            assert response.status_code == 200

    finally:
        with allure.step('Delete created object'):
            requests.delete(f'{URL}/{obj_id}')


@allure.epic('Object API')
@allure.feature('Object Retrieval')
@allure.story('Get object by ID')
@allure.title('Получение объекта по ID')
def test_get_object(object_id):
    with allure.step('Send GET request to retrieve object by ID'):
        response = requests.get(f'{URL}/{object_id}')
    with allure.step('Verify response status code'):
        assert response.status_code == 200
    with allure.step('Verify object name'):
        assert response.json()['name'] == 'tsm object'


@allure.epic('Object API')
@allure.feature('Object Update')
@allure.story('Fully update object')
@allure.title('Полное обновление объекта')
@pytest.mark.medium
def test_put_object(object_id):
    body = {
        "name": "full update object",
        "data": {
            "color": "red",
            "size": "big"
        }
    }
    with allure.step('Send PUT request to fully update object'):
        response = requests.put(f'{URL}/{object_id}', json=body)
        response_data = response.json()
    with allure.step('Verify updated object name'):
        assert response_data['name'] == 'full update object'
    with allure.step('Verify response status code'):
        assert response.status_code == 200


@allure.epic('Object API')
@allure.feature('Object Update')
@allure.story('Partially update object')
@allure.title('Частичное обновление объекта')
def test_patch_object(object_id):
    body = {
        "name": "partially updated object"
    }
    with allure.step('Send PATCH request to partially update object'):
        response = requests.patch(f'{URL}/{object_id}', json=body)
        response_data = response.json()
    with allure.step('Verify updated object name'):
        assert response_data['name'] == 'partially updated object'
    with allure.step('Verify response status code'):
        assert response.status_code == 200


@allure.epic('Object API')
@allure.feature('Object Deletion')
@allure.story('Delete object by ID')
@allure.title('Удаление объекта по ID')
def test_delete_object(object_id):
    with allure.step('Send DELETE request to delete object'):
        response = requests.delete(f'{URL}/{object_id}')
    with allure.step('Verify deletion response status code'):
        assert response.status_code == 200

    with allure.step('Verify object is no longer available'):
        response = requests.get(f'{URL}/{object_id}')
        assert response.status_code == 404
