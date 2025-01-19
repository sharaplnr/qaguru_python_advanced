import requests
from requests import Response
from models.single_user import ResponseData
from models.create_user import CreateUserResponse
from models.update_user import UpdateUserResponse

url: str = 'https://reqres.in/api/users'

def get_user(user_id: str) -> dict:
    response: Response = requests.get(f"{url}/{user_id}")
    response.raise_for_status()
    return response.json()

def create_user(name: str, job: str) -> CreateUserResponse:
    response: Response = requests.post(url, data={"name": name, "job": job})
    response.raise_for_status()
    return CreateUserResponse(**response.json())

def update_user_put_method(user_id: str, updated_data: dict) -> UpdateUserResponse:
    response: Response = requests.put(f"{url}/{user_id}", json=updated_data)
    response.raise_for_status()
    return UpdateUserResponse(**response.json())

def update_user_patch_method(user_id: str, updated_data: dict) -> UpdateUserResponse:
    response: Response = requests.patch(f"{url}/{user_id}", json=updated_data)
    response.raise_for_status()
    return UpdateUserResponse(**response.json())

def delete_user(user_id: str):
    response: Response = requests.delete(f"{url}/{user_id}")
    response.raise_for_status()

def test_validate_data_single_user():
    json_data: dict = get_user("2")
    ResponseData(**json_data)

def test_check_data_single_user_id_2():
    json_data: dict = get_user("2")

    user: ResponseData = ResponseData(**json_data)

    assert user.data.id == 2
    assert user.data.first_name == "Janet"
    assert user.data.last_name == "Weaver"
    assert user.data.email == "janet.weaver@reqres.in"
    assert user.data.avatar == "https://reqres.in/img/faces/2-image.jpg"
    assert user.support.url == "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"
    assert user.support.text == "Tired of writing endless social media content? Let Content Caddy generate it for you."

def test_validate_response_not_exsist_user():
    response: Response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404
    assert response.json() == {}

def test_validate_response_create_user():
    data = {
        "name": "Ilnur",
        "job": "QA Engineer"
    }

    user: CreateUserResponse = create_user(name=data["name"], job=data['job'])
    assert user.name == data['name']
    assert user.job == data['job']
    assert user.id and user.created_at is not None

def test_update_put_user_data():
    updated_data = {
        "name": "Vasya",
        "job": "QA"
    }

    user: CreateUserResponse = create_user(name="Vasiliy", job="Quality Assurance")
    user_info: UpdateUserResponse = update_user_put_method(user.id, updated_data)

    assert user_info.name == updated_data["name"]
    assert user_info.job == updated_data["job"]

def test_update_patch_user_data():
    updated_data = {
        "name": "Vasya",
        "job": "QA"
    }

    user: CreateUserResponse = create_user(name="Vasiliy", job="Quality Assurance")
    user_info: UpdateUserResponse = update_user_patch_method(user.id, updated_data)

    assert user_info.name == updated_data["name"]
    assert user_info.job == updated_data["job"]

def test_delete_user():
    user: CreateUserResponse = create_user(name="John", job="hitman")
    delete_user(user_id=user.id)

    deleted_user_info: Response = requests.get(f"https://reqres.in/api/users/{user.id}")

    assert deleted_user_info.status_code == 404
    assert deleted_user_info.json() == {}




