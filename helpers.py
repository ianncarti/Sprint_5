import random


def random_user_generator():
    random_name = "Amogus" + str(
        random.randint(100, 999))  # рандомный юзернейм из слова "Amogus" и 3-х рандомных цифр
    random_login = random_name + "@yandex.ru"  # на основе сгенерированного юзернейма делаем почту
    random_password = str(random.randint(100000, 999999))  # генерируем пароль из 6 цифр
    return random_name, random_login, random_password