from faker import Faker
from colorama import init, Fore, Style
import sys
import string
import random
# инициализация colorama
init()

python = sys.executable
while True:
    # выбор
    print(Fore.BLUE + "Меню:")
    print(Fore.YELLOW + "1. Cгенерировать фейк юзера")
    print(Fore.GREEN + "2. Генератор паролей")
    
    print(Style.RESET_ALL)

    choice = input("Выберите пункт меню (1-2): ")

    if choice == "1":
        language = input("Какой язык вы предпочитаете? (ru / en): ")
        print("Окей, начинаю генерацию ")
        fake = Faker(language)
        print("--------------------------------")
        print("Общая информация:")
        print(f"ФИО: {fake.name()}")
        print(f"Год рождения: {fake.year()}")
        print(f"Адрес: {fake.address()}")
        print("--------------------------------")
        print("Информация о карте:")
        print(f"Номер карты: {fake.credit_card_number()}")
        print(f"Срок действия: {fake.credit_card_expire()}")
        print(f"CVC код: {fake.credit_card_security_code()}")
        print(f"Банк: {fake.bank()}")
        print("--------------------------------")
        print("Дополнительная информация:")
        print(f"Профессия : {fake.job()}")
        print(f"Комания: {fake.company()}")
        print(f"Email компании: {fake.ascii_company_email()}")
        print(f"Почта: {fake.ascii_free_email()}")
        print(f"Номер телефона: {fake.phone_number()}")
        print(f"Сайт: {fake.hostname()}")
        print(f"Любимый цвет {fake.color_name()}")
        print("--------------------------------")


        print()
        back = input("Введите 'назад', чтобы вернуться в предыдущее меню: ")
        if back == 'назад':
            continue
        
        

    elif choice == "2":
        chars = '@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = input('Количество паролей: ')
        length = input('Длина пароля: ')
        number = int(number)
        length = int(length)
        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            print(password)


        back = input("Введите 'назад', чтобы вернуться в предыдущее меню: ")
        if back == 'назад':
            continue

    else:
        print("Некорректный выбор")