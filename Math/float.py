import math
from functools import lru_cache


# Округление


# Функция round() округляет число до указанного количества знаков
# 		после запятой.
# Принимает: (number, decimal_digits) - число, кол-во после запятой

x = 2.548723
round(x) # -> 3


round(x, 2) # -> 2.55


# Функция ceil() - округляет число до целого в большую сторону.
math.ceil(x) # -> 3

# Функция floor() - округляет число до целого в меньшую сторону.
math.floor(x) # -> 2
