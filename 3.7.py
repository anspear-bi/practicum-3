# -*- coding: utf-8 -*-
"""
3.7
"""
raw = input('Введите число: ')
try:
  num = int(raw)
  print(num)
except ValueError:
  print("Введено не число.")
  
