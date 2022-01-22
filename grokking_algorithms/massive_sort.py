# $2 Lesson


def findSmallest(arr): # Ищет наименьший элемент
	smallest = arr[0] # Для хранения наименьшего элемента
	smallest_index = 0 # Для хранения индекса наименьшего значения
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionSort(arr): # Сортирует массив
	newArr = []
	for i in range(len(arr)):
	# Находит наименьший элемент в массиве и добавляет его в новый массив.
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr


print (selectionSort([5, 3, 6, 2, 10]))