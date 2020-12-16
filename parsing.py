from datetime import datetime as dt
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = 'https://www.python.org/'

"""Получаем html для заданного урла."""


def get_html(url):
    return urlopen(url).read()


""" Данная функция выводит анонс событий с python.org. Анонс событий размещен в блоке 'Upcoming Events.
В блоке перебираем все события в тегах li и выводим на печать события,месяц которых соответствует заданию."""


def parsing_python_org_upcoming_events(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('h2')
    for tag in tags:
        for string in tag.strings:
            if string == 'Upcoming Events':
                upcoming_events_div = tag.parent
    events_list = upcoming_events_div.find_all('li')
    for event in events_list:
        event_date = dt.fromisoformat(event.time['datetime'])
        current_month = dt.today().month
        next_month = current_month + 1 if current_month != 12 else 1
        if event_date.month in (current_month, next_month):
            yield event_date.date(), event.a.string


if __name__ == "__main__":
    html = get_html(URL)
    for event in parsing_python_org_upcoming_events(html):
        print(*event)
