import requests
from faker import Faker
import allure
from url import Urls


fake = Faker()
fakeRU = Faker(locale='ru_RU')


@allure.step("Генерация данных для создания юзера")
def generate_data():
    return {
        "email": f"{fake.user_name()}@mail.ru",
        "password": fake.password(length=10, special_chars=True, digits=True),
        "name": fakeRU.name()
    }

@allure.step("Создание email")
def create_user(body):
    response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=body)
    return response

@allure.step("Изменение данных пользователя")
def changing_user(access_token,field, new_value):
    headers = {'Authorization': access_token}
    payload = {field: new_value}
    response = requests.patch(Urls.BASE_URL + Urls.CHANGE_USER_DATA, headers=headers, json=payload)
    return response

@allure.step("Создание заказа")
def create_order(access_token, component_data):
    headers = {'Authorization': access_token}
    response = requests.post(Urls.BASE_URL + Urls.MAKE_ORDER, headers=headers, json=component_data)
    return response

@allure.step("Получение заказов")
def get_orders(access_token):
    headers = {'Authorization': access_token}
    response = requests.get(Urls.BASE_URL + Urls.GET_ORDERS, headers=headers)
    return response

@allure.step("Удаление курьера в сервисе 'Самокат'")
def delete_user(user_id, access_token):
    headers = {'Authorization': access_token}
    response = requests.delete(Urls.BASE_URL + Urls.DELETE_USER + str(user_id), headers=headers)
    return response