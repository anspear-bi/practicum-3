# -*- coding: utf-8 -*-
"""
3.8
"""
import math

a, b, c = map(float, input("Введите стороны треугольника a, b, c через пробел: ").split())

# Вычисление углов в радианах
A = math.acos((b*2 + c*2 - a*2) / (2 * b * c))
B = math.acos((a*2 + c*2 - b*2) / (2 * a * c))
C = math.acos((a*2 + b*2 - c*2) / (2 * a * b))

# Преобразование в градусы
A_deg, B_deg, C_deg = math.degrees(A), math.degrees(B), math.degrees(C)

print(f"Угол A: {A_deg:.2f} градусов")
print(f"Угол B: {B_deg:.2f} градусов")
print(f"Угол C: {C_deg:.2f} градусов")

