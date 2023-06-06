import requests

# Задание 1
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
need_hero = ['Hulk', 'Captain America', 'Thanos']
powerstats_int = {}
for hero in need_hero:
    for heroes in resp.json():
        if heroes['name'] == hero:
            powerstats_int.update({hero: heroes['powerstats']['intelligence']})
print(f'Самый умный герой {[key for key, value in powerstats_int.items() if value == max(powerstats_int.values())][0]}')


# Задание 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file in path_to_file:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path': file}
            headers = {'Authorization': token}
            res = requests.get(url, params=params, headers=headers)
            url_for_upload = res.json().get('href', '')
            with open(file, 'rb') as f:
                requests.put(url_for_upload, files={'file': f})


file_list = ['1.bmp', '2.bmp', '3.bmp']
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = file_list
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


# Задание 3
url_3 = 'https://api.stackexchange.com//2.3/questions' \
        '?fromdate=1686441600&todate=1686614400&order=desc&sort=activity&tagged=Python&site=stackoverflow'
res = requests.get(url_3)
for value in res.json()['items']:
    print(value['title'])
