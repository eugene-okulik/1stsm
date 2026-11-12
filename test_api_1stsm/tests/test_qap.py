import pytest
from utils.data_generate import make_body


@pytest.mark.parametrize('body', [make_body() for _ in range(3)])
def test_new_object(create_post_endpoint, delete_for_post, body):
    create_post_endpoint.create_new_object(body)
    delete_for_post.object_id = create_post_endpoint.json['id']
    create_post_endpoint.check_object_name(body['name'])
    create_post_endpoint.check_status_code()


def test_get_all_objects(create_get_endpoint):
    create_get_endpoint.get_all_objects()
    create_get_endpoint.check_status_code()


def test_get_one_object(create_get_endpoint, object_id):
    create_get_endpoint.get_one_object(object_id)
    create_get_endpoint.check_status_code()


def test_put_object(create_update_endpoint, object_id):
    body = make_body()
    create_update_endpoint.make_put_update_object(object_id, body)
    create_update_endpoint.check_object_name(body['name'])
    create_update_endpoint.check_status_code()


def test_patch_object(create_update_endpoint, object_id):
    body = make_body()
    create_update_endpoint.make_patch_update_object(object_id, body)
    create_update_endpoint.check_object_name(body['name'])
    create_update_endpoint.check_status_code()


def test_delete_object(create_delete_endpoint, object_id):
    create_delete_endpoint.object_id = object_id
    create_delete_endpoint.delete_object()
    create_delete_endpoint.check_status_code()
