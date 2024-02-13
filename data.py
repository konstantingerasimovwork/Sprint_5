import random
import string

def generate_user_login_data():
    random_user = random.randint(100, 999)
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    return {'name': 'Константин',
            'email': f'konstantin_gerasimov_5{random_user}@yandex.ru',
            'pass': f'{password}'}

def user_test_data():
    return {'email': 'konstantin_gerasimov_5@yandex.ru',
            'pass': '123456'}
