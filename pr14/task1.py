try:
    num = int(input("Введите число: "))
    print(10 / num)
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Ошибка ввода!")