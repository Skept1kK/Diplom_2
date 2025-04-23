import requests
import allure
import pytest
import helper
from data import Data
from url import Urls


class TestUserLogin:

    @allure.title('Возвращение id при успешной аутентификации ')
    def test_login_success(self):
        response = requests.post(Urls.BASE_URL + Urls.LOGIN, json=Data.correct_data)
        assert response.status_code == 200 and response.json().get('success') == True


    @pytest.mark.parametrize('incorrect_data', [helper.generate_data(), Data.incorrect_password ])
    @allure.title('Появление ошибки при аутентификации с невалидными данными')
    def test_login_incorrect__data(self,incorrect_data):
        response = requests.post(Urls.BASE_URL + Urls.LOGIN, json=incorrect_data)
        assert response.status_code == 401 and response.json() == {"success": False,"message": "email or password are incorrect"}


    @pytest.mark.parametrize('incomplete_data', [
        {'login': '', 'password': helper.generate_data()['password']},
        {'login': Data.correct_email, 'password': ''},
    ])
    @allure.title('Появление ошибки при аутентификации с пустым полем логина или пароля')
    def test_login_incomplete_data(self,incomplete_data):
        response = requests.post(Urls.BASE_URL + Urls.LOGIN, json=incomplete_data)
        assert response.status_code == 401 and response.json() == {"success": False,"message": "email or password are incorrect"}