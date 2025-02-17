# -*- coding: utf-8 -*-
"""
3.1
"""
def digit_at_third_position(number):
    number_str = str(number)
    if len(number_str) >= 3:
        return number_str[-3]
    else:
        return "Число меньше трех цифр"

# Пример использования
number = int(input("Введите стоимость биткоина (число): "))
print("Цифра с третьей позиции справа:", digit_at_third_position(number))


