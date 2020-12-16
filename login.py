import re
import time


class LoginVerification:

    def _check_length(self, login):
        if not login:
            return 'Вы не ввели логин'
        if len(login) > 20:
            return 'Слишком длинный логин'
        return True

    """Так как разная логика проверки, делим логин на 3 части"""
    def _split_login(self, login):
        first = login[0]
        middle = login[1:-1]
        last = login[-1] if len(login) > 1 else []
        return first, middle, last

    """1. С помощью build-in методов python проверяем входную строку"""
    def check_with_built_in(self, login):
        status = self._check_length(login)
        if status is True:
            start = time.time()
            first, middle, last = self._split_login(login)
            if (
                first.isalpha()
                and (not middle
                     or middle.isalpha()
                     or middle.isdecimal()
                     or {'.'}.issubset(middle)
                     or {'-'}.issubset(middle))
                and (not last or last.isalpha() or last.isdecimal())
            ):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status

    """2. Проверяем входную строку с помощью сравнивая с подготовленными выборками """
    def check_with_prepared_sets(self, login):
        status = self._check_length(login)
        if status is True:
            start = time.time()
            first, middle, last = self._split_login(login)
            set_for_first = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')  # noqa
            set_for_middle = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890.-')  # noqa
            set_for_last = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')  # noqa
            if (
                set(first).issubset(set_for_first)
                and set(middle).issubset(set_for_middle)
                and set(last).issubset(set_for_last)
            ):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status

    """3. Проверяем входную строку с помощью регулярных выражений """
    def check_with_regular_exp(self, login):
        status = self._check_length(login)
        if status is True:
            start = time.time()
            pattern = (
                '[a-zA-Z]'
                if len(login) == 1
                else '[a-zA-Z]+[0-9a-zA-Z]'
                if len(login) == 2
                else '[a-zA-Z]+[0-9a-zA-Z.-]+[0-9a-zA-Z]'
            )
            if re.fullmatch(pattern, login):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status


if __name__ == "__main__":
    login_from_user = input('Введите логин: ')
    login = LoginVerification()
    print(login.check_with_built_in(login_from_user))
    print(login.check_with_prepared_sets(login_from_user))
    print(login.check_with_regular_exp(login_from_user))