# -*- coding: utf-8 -*-
"""
3.13
"""
N = int(input("Введите количество строк на странице: "))
C = int(input("Введите количество столбцов на странице: "))
record_number = int(input("Введите номер записи в справочнике: "))

# Вычисление номера страницы
page_number = (record_number - 1) // (N * C) + 1

# Вычисление положения записи на странице
position_on_page = (record_number - 1) % (N * C)

# Вычисление номера столбца и записи в столбце
column_number = (position_on_page // N) + 1
row_number = (position_on_page % N) + 1

print(f"Страница {page_number}, столбец {column_number}, строка {row_number}")


