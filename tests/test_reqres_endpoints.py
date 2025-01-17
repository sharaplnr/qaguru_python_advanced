import requests
from requests import Response
from models.single_user import ResponseData
from models.create_user import CreateUserResponse
from models.update_user import UpdateUserResponse

url: str = 'https://reqres.in/api/users/2'
empty_object = {}
def test_validate_data_single_user():
    response: Response = requests.get(url)

    assert response.status_code == 200, 'Received status code is not equal to expected.'

    ResponseData(**response.json())

def test_check_data_single_userid_2():
    response: Response = requests.get(url)

    json: ResponseData = ResponseData(**response.json())

    assert json.data.id == 2
    assert json.data.first_name == "Janet"
    assert json.data.last_name == "Weaver"
    assert json.data.email == "janet.weaver@reqres.in"
    assert json.data.avatar == "https://reqres.in/img/faces/2-image.jpg"
    assert json.support.url == "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"
    assert json.support.text == "Tired of writing endless social media content? Let Content Caddy generate it for you."

def test_validate_response_not_exsist_user():
    response: Response = requests.get('https://reqres.in/api/users/666')

    assert response.json() == empty_object

def test_validate_response_create_user():
    data = {
        "name": "Ilnur",
        "job": "QA Engineer"
    }

    response: Response = requests.post(url="https://reqres.in/api/users", data=data)

    assert response.status_code == 201

    CreateUserResponse(**response.json())

def test_update_put_user_data():
    updated_data = {
        "name": "Vasya",
        "job": "QA"
    }

    user_id: str = CreateUserResponse(**requests.post(url="https://reqres.in/api/users", data={"name": "Ilnur", "job": "QA Engineer"}).json()).id

    response: Response = requests.put(url=f"https://reqres.in/api/users/{user_id}", data=updated_data)
    user_info: UpdateUserResponse = UpdateUserResponse(**response.json())

    assert response.status_code == 200
    assert user_info.name == updated_data["name"]
    assert user_info.job == updated_data["job"]

def test_update_putch_user_data():
    updated_data = {
        "name": "Vasya",
        "job": "QA"
    }

    user_id: str = CreateUserResponse(
        **requests.post(url="https://reqres.in/api/users", data={"name": "Ilnur", "job": "QA Engineer"}).json()).id

    response: Response = requests.patch(url=f"https://reqres.in/api/users/{user_id}", data=updated_data)
    user_info: UpdateUserResponse = UpdateUserResponse(**response.json())

    assert response.status_code == 200
    assert user_info.name == updated_data["name"]
    assert user_info.job == updated_data["job"]

def test_delete_user():
    user_id: str = CreateUserResponse(
        **requests.post(url="https://reqres.in/api/users", data={"name": "Ilnur", "job": "QA Engineer"}).json()).id

    response: Response = requests.delete(url=f"https://reqres.in/api/users/{user_id}")

    assert response.status_code == 204

    response: Response = requests.get(url=f"https://reqres.in/api/users/{user_id}")

    assert response.json() == empty_object


