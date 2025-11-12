import logging

# Настройка логирования
logging.basicConfig(
    filename='user_actions.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

users = {}

def register_user():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if username in users:
        logging.warning(f"Попытка регистрации с существующим именем пользователя: {username}.")
        print("Пользователь с таким именем уже существует.")
    else:
        users[username] = password
        logging.info(f"Пользователь {username} успешно зарегистрирован.")
        print("Пользователь успешно зарегистрирован.")

# Вызов функции регистрации
register_user()
