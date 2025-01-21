import requests
from requests import Response
from models.single_user import ResponseData
from models.create_user import CreateUserResponse
from models.update_user import UpdateUserResponse

data_user = {
            "name": "Ilnur",
            "job": "QA Engineer"
        }

def get_user(url: str, user_id: str) -> dict:
    response: Response = requests.get(f"{url}/{user_id}")
    response.raise_for_status()
    return response.json()

def create_user(url: str, user_info: dict) -> CreateUserResponse:
    response: Response = requests.post(url, json=user_info)
    response.raise_for_status()
    return CreateUserResponse(**response.json())

def update_user_put_method(url: str, user_id: str, updated_data: dict) -> UpdateUserResponse:
    response: Response = requests.put(f"{url}/{user_id}", json=updated_data)
    response.raise_for_status()
    return UpdateUserResponse(**response.json())

def update_user_patch_method(url: str, user_id: str, updated_data: dict) -> UpdateUserResponse:
    response: Response = requests.patch(f"{url}/{user_id}", json=updated_data)
    response.raise_for_status()
    return UpdateUserResponse(**response.json())

def delete_user(url: str, user_id: str):
    response: Response = requests.delete(f"{url}/{user_id}")
    response.raise_for_status()

class TestReqres:
    url: str = 'https://reqres.in/api/users'

    def test_validate_data_single_user(self):
        json_data: dict = get_user(self.url, "2")
        ResponseData(**json_data)

    def test_check_data_single_user_id_2(self):
        json_data: dict = get_user(self.url, "2")

        user: ResponseData = ResponseData(**json_data)

        assert user.data.id == 2
        assert user.data.first_name == "Janet"
        assert user.data.last_name == "Weaver"
        assert user.data.email == "janet.weaver@reqres.in"
        assert user.data.avatar == "https://reqres.in/img/faces/2-image.jpg"
        assert user.support.url == "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"
        assert user.support.text == "Tired of writing endless social media content? Let Content Caddy generate it for you."

    def test_validate_response_not_exsist_user(self):
        response: Response = requests.get(f"{self.url}/23")
        assert response.status_code == 404
        assert response.json() == {}

    def test_validate_response_create_user(self):
        data = {
            "name": "Ilnur",
            "job": "QA Engineer"
        }

        user: CreateUserResponse = create_user(self.url, user_info=data_user)
        assert user.name == data['name']
        assert user.job == data['job']
        assert user.id and user.created_at is not None

    def test_update_put_user_data(self):
        updated_data = {
            "name": "Vasya",
            "job": "QA"
        }

        user: CreateUserResponse = create_user(self.url,user_info=data_user)
        user_info: UpdateUserResponse = update_user_put_method(self.url, user.id, updated_data)

        assert user_info.name == updated_data["name"]
        assert user_info.job == updated_data["job"]

    def test_update_patch_user_data(self):
        updated_data = {
            "name": "Vasya",
            "job": "QA"
        }

        user: CreateUserResponse = create_user(self.url, user_info=data_user)
        user_info: UpdateUserResponse = update_user_patch_method(self.url, user.id, updated_data)

        assert user_info.name == updated_data["name"]
        assert user_info.job == updated_data["job"]

    def test_delete_user(self):
        user: CreateUserResponse = create_user(self.url, user_info=data_user)
        delete_user(self.url, user_id=user.id)

        deleted_user_info: Response = requests.get(f"{self.url}/{user.id}")

        assert deleted_user_info.status_code == 404
        assert deleted_user_info.json() == {}

class TestFastApi:
    url = "http://localhost:8000/api/users"
    def test_validate_data_single_user(self):
        response: Response = requests.get(f"{self.url}/2")

        assert response.status_code == 200, 'Received status code is not equal to expected.'
        ResponseData(**response.json())

    def test_validate_response_create_user(self):
        user: CreateUserResponse = create_user(self.url, user_info=data_user)
        assert user.name == data_user.get("name")
        assert user.job == data_user.get("job")
        assert user.id and user.created_at is not None

    def test_validate_response_not_exsist_user(self):
        response: Response = requests.get(f"{self.url}/23")

        assert response.status_code == 404
        assert response.json() == {}

    def test_update_put_user_data(self):
        updated_data = {
            "name": "Vasya",
            "job": "QA"
        }

        user_info: UpdateUserResponse = update_user_put_method(self.url,2, updated_data)

        assert user_info.name == updated_data["name"]
        assert user_info.job == updated_data["job"]

    def test_update_patch_user_data(self):
        updated_data = {
            "name": "Vasya",
            "job": "QA"
        }

        user_info: UpdateUserResponse = update_user_patch_method(self.url, 2, updated_data)

        assert user_info.name == updated_data["name"]
        assert user_info.job == updated_data["job"]

    def test_delete_user(self):
        response: Response = requests.delete(f"{self.url}/3")

        assert response.json() == {}
