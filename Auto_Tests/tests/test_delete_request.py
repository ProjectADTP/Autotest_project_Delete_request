from requests import Response

from crud_operations.api import GMAPI


# Класс с тестами
class TestCreatePlace:
    # Тест создания нового места
    def test_create_new_place(self):
        # Объект класса Google Maps API
        gmapi = GMAPI()

        # Вызов метода создания нового места
        print("\nМетод POST")
        result_post: Response = gmapi.create_new_place()
        print(result_post.json())

        # Вызов метода получения данных о месте по place_id
        print("\nМетод Get после Post")
        result_get: Response = gmapi.get_place_by_place_id(result_post.json()["place_id"])
        print(result_get.json())

        # Вызов метода обновления данных о месте по place_id
        print("\nМетод Put")
        result_put: Response = gmapi.update_place_by_place_id(result_post.json()["place_id"])
        print(result_put.json())

        # Вызов метода получения данных о месте по place_id
        print("\nМетод Get после Put")
        result_get: Response = gmapi.get_place_by_place_id(result_post.json()["place_id"])
        print(result_get.json())

        # Вызов метода обновления данных о месте по place_id
        print("\nМетод Delete")
        result_put: Response = gmapi.delete_place_by_place_id(result_post.json()["place_id"])
        print(result_put.json())

        # Вызов метода получения данных о месте по place_id
        print("\nМетод Get после Delete")
        result_get: Response = gmapi.get_place_by_place_id(result_post.json()["place_id"])
        print(result_get.json())