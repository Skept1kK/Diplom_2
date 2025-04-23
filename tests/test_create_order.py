import helper
import allure
from conftest import create_user
from data import Component

class TestCreateOrder:

    @allure.description("Создание заказа авторизованным пользователем")
    @allure.title("Проверка создания заказа с корректными ингредиентами")
    def test_create_order_with_authorization(self, create_user):
        access_token = create_user[1]
        response = helper.create_order(access_token, Component.correct_component)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Попытка Создание заказа без авторизации")
    @allure.title("Проверка создания заказа с корректными ингредиентами")
    def test_create_order_without_authorization(self):
        response = helper.create_order(None, Component.correct_component)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Попытка Создание заказа без авторизации")
    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_component_without_authorization(self):
        response = helper.create_order(None, None)
        assert response.status_code == 400 and response.json() == {'success': False,'message': 'Ingredient ids must be provided'}

    @allure.description("Создание заказа авторизованным пользователем")
    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_component_authorization(self, create_user):
        access_token = create_user[1]
        response = helper.create_order(access_token, None)
        assert response.status_code == 400 and response.json() == {'success': False,'message': 'Ingredient ids must be provided'}

    @allure.description("Попытка Создание заказа без авторизации")
    @allure.title("Проверка создания заказа с некорректными ингредиентами")
    def test_create_order_incorrect_component_with_authorization(self, create_user):
        access_token = create_user[1]
        response = helper.create_order(access_token, Component.incorrect_component)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
        assert 'Internal Server Error' in response.text, "Expected 'Internal Server Error' in response text"