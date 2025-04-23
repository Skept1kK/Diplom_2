import allure
import requests
import helper
from url import Urls
from conftest import create_user



class TestCreateUser:

    @allure.title("Проверка создания пользователя")
    def test_create_user(self,create_user):
        body = helper.generate_data()
        response = helper.create_user(body)
        assert response.status_code == 200 and response.json().get('success') == True


    @allure.title("Создание пользователя с существующим email")
    def test_create_user_second_email (self,create_user):
        body = helper.generate_data()
        helper.create_user(body)
        payload = {
            'email': body['email'],
            'password': helper.generate_data()['password'],
            'name': helper.generate_data()['name']
        }
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=payload)
        assert response.status_code == 403 and response.json() == {'success': False, 'message': 'User already exists'}


    @allure.title("Создание пользователя без email")
    def test_create_user_without_email(self,create_user):
        payload = {
            'email': "",
            'password': helper.generate_data()['password'],
            'name': helper.generate_data()['name']
        }
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=payload)
        assert response.status_code == 403 and response.json() == {'success': False, 'message': 'Email, password and name are required fields'}

    @allure.title("Создание пользователя без password")
    def test_create_user_without_password(self,create_user):
        payload = {
            'email': helper.generate_data()['email'],
            'password': "",
            'name': helper.generate_data()['name']
        }
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=payload)
        assert response.status_code == 403 and response.json() == {'success': False, 'message': 'Email, password and name are required fields'}

    @allure.title("Создание пользователя без name")
    def test_create_user_without_name(self,create_user):
        payload = {
            'email': helper.generate_data()['email'],
            'password': helper.generate_data()['password'],
            'name': ""
        }
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=payload)
        assert response.status_code == 403 and response.json() == {'success': False,'message': 'Email, password and name are required fields'}