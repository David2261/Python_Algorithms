import sys
from collections import defaultdict, deque

# Установка максимального рекурсивного уровня
sys.setrecursionlimit(200000)

class TrieNode:
	def __init__(self):
		self.children = {}
		self.popularities = []

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word, popularity):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
			node.popularities.append(popularity)

	def autocomplete(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node.children:
				return -1
			node = node.children[char]
		if node.popularities:
			return max(node.popularities)
		return -1

def process_commands(N, Q, words, commands):
	trie = Trie()
	for word, popularity in words:
		trie.insert(word, popularity)

	t = ""
	results = []

	for command in commands:
		if command[0] == '+':
			t += command[2]
		elif command[0] == '-':
			t = t[:-1]
		results.append(trie.autocomplete(t))

	return results

if __name__ == "__main__":
	input = sys.stdin.read
	data = input().strip().split('\n')

	N, Q = map(int, data[0].split())

	words = []
	for i in range(1, N + 1):
		parts = data[i].split()
		word = parts[0]
		popularity = int(parts[1])
		words.append((word, popularity))

	commands = data[N + 1:]

	results = process_commands(N, Q, words, commands)
	print('\n'.join(map(str, results)))
