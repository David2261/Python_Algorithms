def format_text(text):
	words = text.replace(',', ', ').split()

	i = 0
	while True:
		try:
			i = words.index(',', i)
			words[i - 1] += words.pop(i)
		except ValueError:
			break

	max_word_length = max(len(word.rstrip(',')) for word in words)
	max_line_length = max_word_length * 3

	lines = []
	cur_line = ''

	for word in words:
		if len(cur_line) + len(word) + (bool(cur_line)) <= max_line_length:
			if cur_line:
				cur_line += ' '
			cur_line += word
		else:
			lines.append(cur_line)
			cur_line = word
	if cur_line:
		lines.append(cur_line)
	
	return '\n'.join(lines)

if __name__ == '__main__':
	import sys
	input = sys.stdin.read().strip()
	formatted_text = format_text(input)
	print(formatted_text)
