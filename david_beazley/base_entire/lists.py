import sys

# Проверка кол-ва аргументов командной строки:
if len(sys.argv) != 2:
	print("Пожалуйста, укажите имя файла")
	raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
f.close()

# Преобразование из строки в числа с плавающей точкой
fvalues = [float(line) for line in lines]

print("Минимальное значение: ", min(fvalues))
print("Максимальное значение: ", max(fvalues))

"""
python3.11 lists.py test.txt
Минимальное значение:  1232477893.0
Максимальное значение:  8048647870534543.0
"""
