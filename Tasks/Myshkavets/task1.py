import math
import random

# Функция для преобразования градусов Цельсия в градусы Фаренгейта
def celsius_to_fahrenheit():
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")

# Функция для вычисления площади окружности
def calculate_circle_area():
    radius = float(input("Введите радиус окружности: "))
    area = math.pi * radius ** 2
    print(f"Площадь окружности с радиусом {radius} равна {area}")

# Функция для преобразования километров в час в метры в секунду
def km_to_mps():
    kilometers_per_hour = float(input("Введите скорость в километрах в час: "))
    meters_per_second = kilometers_per_hour * 1000 / 3600
    print(f"{kilometers_per_hour} км/час = {meters_per_second} м/сек")

# Функция для конвертации суммы денег из долларов США в покупку
def usd_to_purchase():
    usd_amount = float(input("Введите сумму в долларах США: "))
    exchange_rate = 2.5  # Пример: 1 доллар США = 2.5 покупки
    purchase_equivalent = usd_amount * exchange_rate
    print(f"{usd_amount} долларов США эквивалентно {purchase_equivalent} покупке")

# Функция для генерации случайного числа в заданном диапазоне
def generate_random_number():
    left_boundary = int(input("Введите левую границу диапазона: "))
    right_boundary = int(input("Введите правую границу диапазона: "))
    random_number = random.randint(left_boundary, right_boundary)
    print(f"Случайное число в диапазоне от {left_boundary} до {right_boundary}: {random_number}")

# Выбор программы для выполнения
while True:
    print("Выберите программу для выполнения:")
    print("1. Преобразовать градусы Цельсия в градусы Фаренгейта")
    print("2. Вычислить площадь окружности")
    print("3. Преобразовать километры в час в метры в секунду")
    print("4. Конвертировать сумму денег из долларов США в покупку")
    print("5. Генерировать случайное число в заданном диапазоне")
    print("6. Выйти из программы")
    
    choice = input("Введите номер программы (1/2/3/4/5/6): ")
    
    if choice == '1':
        celsius_to_fahrenheit()
    elif choice == '2':
        calculate_circle_area()
    elif choice == '3':
        km_to_mps()
    elif choice == '4':
        usd_to_purchase()
    elif choice == '5':
        generate_random_number()
    elif choice == '6':
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите программу снова.")
