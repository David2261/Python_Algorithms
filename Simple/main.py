"""Самые оснавные функции в python"""


# Лист
class List_Square:
	numbers = [2, 3, 4, 21, 34, 65, 28, 93]
	squares = (n**2 for n in numbers)
	#print(squares)
	# <generator object <genexpr> at 0x00000209FB6B99C8>
	list_squares = list(squares)
	#print(list_squares)
# check_list = List_Square()
# print(check_list)


# Кортеж
class Tup:
	numbers = [2, 3, 4, 21, 34, 65, 28, 93]
	numbers = tuple(numbers)

	#print(num)
# Tup()


# Словарь
class Dict_List:
	color_counts = [
		('red', 2),
		('green', 1),
		('blue', 3),
		('purple', 5)
	]
	colors = {}
	for color, n in color_counts:
		colors[color] = n
	#print(colors)
# Dict_List()

# Набор
class Set_List(Tup):
	numbers = [1, 1, 2, 3, 5, 8]
	if bool(numbers):
		numbers = set(numbers)
		print(f'Набор {numbers}')
	else:
		print("Набор пуст")
Set_List()

# Подсчет количество элементов
def palindromic():
    """Возвращает True, если последовательность является палиндромом."""
    sequence = str('Texet')

    for i, item in enumerate(sequence):
        if item != sequence[-(i+1)]:
            return False
    return True
palindromic()

# Сортировка
numbers = [1, 8, 2, 13, 5, 3, 1]
words = ["python", "is", "lovely"]
print(sorted(words))

print(sorted(numbers, reverse=True))

print(type(palindromic))