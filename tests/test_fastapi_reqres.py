import requests
from requests import Response
from models.single_user import ResponseData
from models.create_user import CreateUserResponse
from models.update_user import UpdateUserResponse

url: str = 'http://0.0.0.0:8000/api/users/2'
empty_object = {}
def test_validate_data_single_user():
    response: Response = requests.get(url)

    assert response.status_code == 200, 'Received status code is not equal to expected.'

    ResponseData(**response.json())