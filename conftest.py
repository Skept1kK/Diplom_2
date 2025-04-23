import pytest
import helper


@pytest.fixture
def create_user():
    body = helper.generate_data()
    response = helper.create_user(body)
    assert response.status_code == 200 and response.json()["success"] is True
    user_id = response.json().get('user', {}).get('id')
    access_token = response.json().get('accessToken')
    yield user_id, access_token

    if user_id:
        helper.delete_user(user_id, access_token)