from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self, file_path: str):
        files_url = file_path
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

    # def upload(self, file_path: str):
    #     """Метод загружает файлы по списку file_list на яндекс диск"""


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            status_resalt = "Success"
            print(status_resalt)
        return status_resalt

def pushing_files_to_yandex (name_file):
    putloader = YaUploader(token)
    if putloader.upload_file_to_disk(f'Netologi/{name_file}', f'{name_file}') == "Success":
        print(f' Файл {name_file} отправлен на яндекс диск в директорию Netologi')
        cod_resalt = 201
        return cod_resalt

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    token = 'AQAAAABbqfAeAADLW0ZHggdGL0GIpWWHzWBa9gI'
    # uploader = YaUploader(token)
    # pprint(uploader.get_files_list(path_to_file))
    print ('Результаты работы')
    print(pushing_files_to_yandex('File_for_test.txt'))
