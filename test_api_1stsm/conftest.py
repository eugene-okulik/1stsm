import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import PutUpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from utils.data_generate import make_body


@pytest.fixture()
def create_get_endpoint():
    return GetObject()


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def create_update_endpoint():
    return PutUpdateObject()


@pytest.fixture()
def create_delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id():
    create = CreateObject()
    delete = DeleteObject()

    body = make_body()
    create.create_new_object(body)
    delete.object_id = create.json['id']
    yield delete.object_id
    delete.delete_object()


@pytest.fixture()
def delete_for_post():
    delete = DeleteObject()
    yield delete

    if delete.object_id is not None:
        delete.delete_object()
