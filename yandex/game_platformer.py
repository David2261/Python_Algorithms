def final_positions_count(N, commands):
	def move(commands): 
		x = 0
		direction = 0
		for command in commands:
			if command == 'F':
				if direction == 0:
					x += 1
				elif direction == 2:
					x -= 1
			elif command == 'R':
				direction = (direction + 1) % 4
			elif command == 'L':
				direction = (direction - 1) % 4
		return x

	unique_positions = set()
	for i in range(N):
		for replacement in 'FRL':
			if commands[i] != replacement:
				new_commands = commands[:i] + replacement + commands[i+1:]
				position = move(new_commands)
				unique_positions.add(position)
	return len(unique_positions)

N = int(input())
commands = input().strip()
print(final_positions_count(N, commands))