def recover_password(sequence, chars, k):
	seq_set = set(sequence)
	password = ''

	for i in range(len(sequence)):
		window = ''
		for j in range(i, len(sequence)):
			window += sequence[j]
			if all(c in window for c in chars) and len(window) <= k:
				if len(window) > len(password):
					password = window
				elif len(window) == len(password) and sequence.index(window) > sequence.index(password):
					password = window

	if not password:
		return -1
	else:
		return password

sequence = input()
char_set = input()
max_length = int(input())

password = recover_password(sequence, char_set, max_length)

print(password)