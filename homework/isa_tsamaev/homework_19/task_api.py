import requests


def get_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    return response


def new_object():
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "mega object",
        "data": {
            "color": "blue",
            "size": "small"
        }
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', headers=headers, json=body)
    return response.json()['id']


def get_one_object(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response


def put_update_object():
    object_id = new_object()
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "full update object",
        "data": {
            "color": "red",
            "size": "big"
        }
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}', headers=headers, json=body)
    response_data = response.json()
    print(response.status_code)
    print(response_data)
    assert response_data['name'] == 'full update object'
    delete_object(object_id)


def patch_update_object():
    object_id = new_object()
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "partially updated object"
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', headers=headers, json=body)
    response_data = response.json()
    print(response.status_code)
    print(response_data)
    assert response_data['name'] == 'partially updated object'
    delete_object(object_id)


def delete_object(obj_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    return response.status_code


print(get_all_objects().json())
put_update_object()
patch_update_object()
print(get_all_objects().json())
