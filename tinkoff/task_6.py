from collections import defaultdict, deque

def min_time(n, times, dependencies):
	graph = defaultdict(list)
	in_degree = [0] * (n + 1)
	
	for i in range(1, n + 1):
		for dep in dependencies[i]:
			graph[dep].append(i)
			in_degree[i] += 1
	
	queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
	
	time = [0] * (n + 1)
	for i in range(1, n + 1):
		time[i] = times[i - 1]
	
	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			time[neighbor] = max(time[neighbor], time[node] + times[neighbor - 1])
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				queue.append(neighbor)
	
	return max(time)

n = int(input())
times = []
dependencies = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
	time, *deps = map(int, input().split())
	times.append(time)
	dependencies[i] = deps

print(min_time(n, times, dependencies))