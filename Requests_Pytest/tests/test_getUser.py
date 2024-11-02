import pytest
from Requests_Pytest.utils.api import APIs
import uuid


@pytest.fixture(scope='module')
def apis():
    return APIs()


def test_getuser_validation(apis):
    response = apis.get('users')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_user(apis, load_json_data):
    # hardcoded data is not standards will store user in data folder and using apis we will fetch data from json file
    # user_data ={
    #     "name": "ramcharn",
    #     "username": "ram",
    #     "email": "ram#charan@gmail",
    # }
    user_data = load_json_data['new_user']
    # generate unique email
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email

    response = apis.post('users', user_data)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'ramcharan'

#     to verify if the user is created check with get
    id = response.json()['id']
    res = apis.get('users/10')
    # res = apis.get('users/id')
    print(res.json())
    assert res.json()['name'] == 'Clementina DuBuque'

#  in realtime it works here it doesnt


def test_update_user(apis):
    user_data = {
        "name": "ram charan chandra",
        "username": "ram",
        "email": "ram#charan@gmail"
    }
    response = apis.put('users/1', user_data)
    print(response.json())
    print(response.status_code)
    assert response.json()['name'] == "ram charan chandra"
    assert response.status_code == 200


def test_delete_user(apis):
    response = apis.delete('users/1')
    print(response.json())
    assert response.status_code == 200
