from urllib.request import urlopen



URL = 'https://www.python.org/'


"""Получаем html для заданного урла."""
def get_html(url):
    return urlopen(url).read()
