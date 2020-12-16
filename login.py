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


if __name__ == "__main__":
    login_from_user = input('Введите логин: ')
    login = LoginVerification()
    print(login.check_with_built_in(login_from_user))