# Программа на Python для сингла деистры
# алгоритм поиска кратчайшего пути. Программа
# для матричного представления графа

import sys


class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Вершина \tРасстояние от источника")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # Служебная функция для поиска вершины с
    # минимальное значение расстояния от множества вершин
    # еще не включен в дерево кратчайших путей
    def minDistance(self, dist, sptSet):
 
        # Инициализировать минимальное расстояние для следующего узла
        min = sys.maxsize
 
        # Искать не ближайшую вершину не в
        # дерево кратчайших путей
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Функция, реализующая единый источник Дейкстры
    # алгоритм кратчайшего пути для представленного графа
    # использование представления матрицы смежности
    def deistra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Выбираем вершину с минимальным расстоянием от
            # набор еще не обработанных вершин.
            # x всегда равно src на первой итерации
            x = self.minDistance(dist, sptSet)
 
            # Поместите вершину минимального расстояния в
            # дерево кратчайших путей
            sptSet[x] = True
 
            # Обновить значение расстояния для соседних вершин
            # выбранной вершины, только если текущая
            # расстояние больше нового расстояния и
            # вершина не входит в дерево кратчайших путей
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.deistra(0)