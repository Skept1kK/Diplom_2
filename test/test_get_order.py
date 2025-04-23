import helper
import allure
from conftest import create_user
from data import Component



class TestGetOrder:

    @allure.title("Получение заказа авторизованным пользователем ")
    def test_get_order_with_authorization(self, create_user):
        access_token = create_user[1]
        requests_create_order =helper.create_order(access_token, Component.correct_component)
        created_order_number = requests_create_order.json().get('order', {}).get('number')
        response_get_order = helper.get_orders(access_token)
        retrieved_order_number = response_get_order.json().get('orders', [{}])[0].get('number')
        assert response_get_order.status_code == 200, "Expected status code 200"
        assert retrieved_order_number == created_order_number, f"Expected order number {created_order_number}, but got {retrieved_order_number}"

    @allure.title("Получение заказа пользователем без авторизации")
    def test_get_order_without_authorization(self):
        response = helper.get_orders(None)
        assert response.status_code == 401 and response.json() == {'success': False, 'message': 'You should be authorised'}
