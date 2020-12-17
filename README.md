# Спиридонов Роман (Speccy-Rom)
Мое Резюме: https://hh.ru/resume/4a35d0b9ff0843acf50039ed1f644e61787345

## Тестовое задание

### Задание 1. :white_check_mark:
В системе авторизации есть ограничение: логин должен начинаться
с латинской буквы, состоять из латинских букв, цифр, точки и минуса, но
заканчиваться только латинской буквой или цифрой; минимальная длина
логина — не ограничена, максимальная — 20. Напишите код, проверяющий
соответствие входной строки этому правилу. Придумайте несколько способов
решения задачи и сравните их.

### Задание 2. white_check_mark:
Напишите тест на функцию из задания №1

### Задание 3. white_check_mark:
Разработайте скрипт на Python, который будет выводить в консоль
информацию о событиях этого и следующего месяца, анонсированных на
главной странице python.org. Вывод информации оформите по своему
усмотрению. Выбор библиотек на ваше усмотрение. Желательно завернуть
скрипт в докер контейнер, чтобы его можно было проверить на любой машине.

### Выполните пункты ниже
Для проверки
- склонируйте проект с реппозитория GitHub :arrow_down:
    ```
    git clone https://github.com/Speccy-Rom/Speccy_Test_Task.git
    ```
- перейдите в директорию Speccy_Test_Task/ :arrow_down:
    ```
    cd Speccy_Test_Task/
    ```
- соберите docker образ :arrow_down:
    ```
    docker build -t speccy-test .
    ```
- запуск проверки логина :arrow_down:
    ```
    docker run --rm -it speccy-test python3 login.py
    ```
- запуск тестов  :arrow_down:
    ```
    docker run --rm -it speccy-test pytest
    ```
- запуск парсера python.org  :arrow_down:
    ```
    docker run --rm -it speccy-test python3 parsing.py
    ```