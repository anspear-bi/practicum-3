# -*- coding: utf-8 -*-
"""
3.4
"""
X, Y, N = map(int, input("Введите X, Y и N через пробел: ").split())
total_cents = (X * 100 + Y) * N
R, K = divmod(total_cents, 100)
print(f"{R} руб. {K} коп.")


