import urllib.request
import urllib.parse
import json
import re


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


# Формирование базы фильмов:
# --------------------------------------------------------

def create_bd():
    movies_list = []
    ed = int(input('Please, enter required value of database: '))
    num = 0

    while num < ed:
        try:
            method_str_group = '/movie/%s' % num
            rct = make_tmdb_api_request(method=method_str_group, api_key='aa7971b2460ccafcd6d0d480db1b5b97')
            num += 1
            movies_list.append(rct)
            print(num, rct)
        except urllib.error.HTTPError:
            num += 1
            ed += 1
    print(movies_list)


# Сохранение и загрузка в json
# --------------------------------------------------------

def write_json_bd():
    with open('movie_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(movies_list, ensure_ascii=False))

def read_json_bd():
    with open('movie_data.json', 'r', encoding='utf-8') as file:
        global data
        data = json.load(file)


# Поиск фильма по названию
# --------------------------------------------------------

def find_film():
    global ipt
    ipt = str(input('Enter the title: '))
    for i in range(0, len(data)):
        temp = re.findall(ipt, data[i]['title'], re.IGNORECASE)
        if len(temp) > 0:
            print(' -> ', data[i]['title'])


# Рекомендации фильмов по названию
# --------------------------------------------------------
# Не завершено

