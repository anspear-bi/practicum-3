# -*- coding: utf-8 -*-
"""
3.9
"""
def passer_rating(ATT, COMP, YDS, TD, INT):
    if ATT == 0:
        return 0  # Избегаем деления на ноль
    a = ((COMP / ATT) - 0.3) * 5
    b = ((YDS / ATT) - 3) * 0.25
    c = (TD / ATT) * 20
    d = 2.375 - ((INT / ATT) * 25)

    rating = (a + b + c + d) / 6 * 100
    return max(0, min(158.3, rating))

# Ввод параметров
ATT = int(input("Введите количество попыток передачи: "))
COMP = int(input("Введите количество завершённых передач: "))
YDS = int(input("Введите количество ярдов: "))
TD = int(input("Введите количество тачдаунов: "))
INT = int(input("Введите количество перехватов: "))

# Вычисление и вывод рейтинга
rating = passer_rating(ATT, COMP, YDS, TD, INT)
print(f"Рейтинг квотербека: {rating:}")




