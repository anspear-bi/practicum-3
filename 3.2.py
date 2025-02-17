# -*- coding: utf-8 -*-
"""
3.2
"""
def convert_seconds_to_time(seconds):
    if 1 <= seconds <= 86400:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds_remaining = seconds % 60
        return hours, minutes, seconds_remaining
    else:
        return "Введите число в диапазоне от 1 до 86400"

# Пример использования
seconds_input = int(input("Введите количество секунд (от 1 до 86400): "))
time = convert_seconds_to_time(seconds_input)

if isinstance(time, tuple):
    print(f"Текущая время: {time[0]} часов, {time[1]} минут, {time[2]} секунд")
else:
    print(time)
    

