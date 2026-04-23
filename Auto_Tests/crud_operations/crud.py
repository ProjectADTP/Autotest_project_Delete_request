import requests


class CRUD:
    # Заголовок с указанием json расширения
    headers = {'Content-Type': 'application/json'}
    # Куки
    cookie = None

    # Get-запрос с указанием адреса, заголовка, куков и возвращающий ответ
    @staticmethod
    def get(url):
        response = requests.get(url, headers=CRUD.headers, cookies=CRUD.cookie)
        return response

    # Post-запрос с указанием адреса, тела в формате json, заголовка, куков и возвращающий ответ
    @staticmethod
    def post(url, body):
        response = requests.post(url, json=body, headers=CRUD.headers, cookies=CRUD.cookie)
        return response

    # Put-запрос с указанием адреса, тела в формате json, заголовка, куков и возвращающий ответ
    @staticmethod
    def put(url, body):
        response = requests.put(url, json=body, headers=CRUD.headers, cookies=CRUD.cookie)
        return response

    # Delete-запрос с указанием адреса, тела в формате json, заголовка, куков и возвращающий ответ
    @staticmethod
    def delete(url, body):
        response = requests.delete(url, json=body, headers=CRUD.headers, cookies=CRUD.cookie)
        return response
