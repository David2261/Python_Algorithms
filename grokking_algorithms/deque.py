# $4 Lesson
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]


def search(name):
	search_queue = deque() # Создание новой очереди
	search_queue += graph["you"] # Все соседи доб. в очередь поиска
	# Этот массив используется для отслеживания уже проверенных людей
	searched = []
	while search_queue: # пока очередь не пуста...
		person = search_queue.popleft() # Из очереди извлекается 1 чел.
		if not person in searched:
			if person_is_seller(person):
				# Проверяем, является ли этот человек продавцом манго
				print(person + "is a mango seller!") # Да, это продавец
				return True
			else:
				search_queue += graph[person] # Доб. в очередь поиска
				searched.append(person) # Чел. помечается как уже проверенный
	return False # Если выполнение дошло до этой строки, то продавца нет

search("you")